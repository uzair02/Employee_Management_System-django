from django.urls import path
from . import views

urlpatterns = [
    #for the login page
    path('login/', views.admin_login, name='login'),
    #for the logout page
    path('logout/', views.admin_logout, name='logout'),
    #for the dashboard page
    path('', views.dash, name='dash'),
    #for the documentation page
    path('documentation/', views.documentation, name='documentation'), 
]