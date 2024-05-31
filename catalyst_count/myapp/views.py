# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User


@login_required
def upload_data_view(request):
    # Your logic for upload data
    return render(request, 'upload_data.html')

@login_required
def query_builder_view(request):
    # Your logic for query builder
    return render(request, 'query_builder.html')

@login_required
def user_list_view(request):
    users = User.objects.filter(is_superuser='False')
    return render(request, 'user_list.html', {'users': users})

def remove_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user_list')