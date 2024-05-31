# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.decorators import login_required


@csrf_exempt
def upload_chunk(request):
    if request.method == 'POST':
        file = request.FILES['file']
        chunk_number = int(request.POST['chunk_number'])
        total_chunks = int(request.POST['total_chunks'])
        filename = request.POST['filename']

        upload_dir = 'uploads/temp/'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        chunk_path = os.path.join(upload_dir, f'{filename}.part{chunk_number}')
        with open(chunk_path, 'wb') as chunk_file:
            for chunk in file.chunks():
                chunk_file.write(chunk)
        
        if chunk_number == total_chunks:
            final_path = os.path.join('uploads/', filename)
            with open(final_path, 'wb') as final_file:
                for i in range(1, total_chunks + 1):
                    chunk_path = os.path.join(upload_dir, f'{filename}.part{i}')
                    with open(chunk_path, 'rb') as chunk_file:
                        final_file.write(chunk_file.read())
                    os.remove(chunk_path)
            
            Upload.objects.create(file=final_path)
            
            # Parse the CSV file and update the database
            with open(final_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    CompanyData.objects.create(
                        keyword=row['Keyword'],
                        industry=row['Industry'],
                        year_founded=int(row['Year Founded']),
                        city=row['City'],
                        state=row['State'],
                        country=row['Country'],
                        employees_from=int(row['Employees (From)']),
                        employees_to=int(row['Employees (To)'])
                    )
            
            return JsonResponse({'message': 'File uploaded and processed successfully'})
        
        return JsonResponse({'message': 'Chunk uploaded successfully'})
    return HttpResponse(status=405)

@login_required
def upload_data_view(request):
    return render(request, 'upload_data.html')

@login_required
def query_builder_view(request):
    return render(request, 'query_builder.html')

@login_required
def user_list_view(request):
    users = User.objects.filter(is_superuser='False')
    return render(request, 'user_list.html', {'users': users})

def add_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            User.objects.create_user(username=username, password=password)
            request.session['success_message'] = 'User added successfully!'
            return redirect('user_list')
        else:
            return HttpResponse("Invalid data", status=400)
    return redirect('user_list')

@login_required
def remove_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        request.session['success_message'] = 'User removed successfully!'
    except User.DoesNotExist:
        request.session['success_message'] = 'User does not exist!'
    return redirect('user_list')