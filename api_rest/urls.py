from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'), #NOTE - URL path to show all users
    path('<str:nick>', views.get_by_nick), #NOTE - URL path to search directly for the user's nick
    path('data/', views.user_manager) #NOTE - URL path to manage users data
]