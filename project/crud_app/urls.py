from django.urls import path
from .views import add_job,show_job,update_job,delete_job
urlpatterns = [
    path('add/',add_job,name='add_url'),
    path('show/',show_job,name='show_url'),
    path('update/<int:pk>/',update_job,name='update_url'),
    path('delete/<int:pk>/',delete_job,name='delete_url')
]