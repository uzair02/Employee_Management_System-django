from django.urls import path
from . import views

urlpatterns = [
    #To add new employee
    path('create/', views.create, name='create'),

    #To read employees
    path('read/', views.read, name='read'),

    #To edit employees
    path('edit/<int:pk>', views.edit, name='edit'),

    #To delete employees
    path('delete/<int:pk>', views.delete, name='delete'),
]