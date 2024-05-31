# urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from myapp.views import upload_data_view, query_builder_view, user_list_view,remove_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Includes allauth URLs
    path('', TemplateView.as_view(template_name='welcome.html'), name='welcome'),  # Welcome page URL
    path('upload_data/', upload_data_view, name='upload_data'),  # Upload Data view
    path('query_builder/', query_builder_view, name='query_builder'),  # Query Builder view
    path('user_list/', user_list_view, name='user_list'), 
    path('remove_user/<int:user_id>/',remove_user,name='remove_user')
]
