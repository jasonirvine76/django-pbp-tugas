from django.contrib import admin
from django.urls import path, include
from todolist.views import create_task, is_finished, is_not_finished, login_user, logout_user, todolist, register, delete

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('<int:id>', delete, name = 'delete'),
    path('<int:id>/selesai', is_finished, name ='finished'),
    path('<int:id>/belum-selesai', is_not_finished, name='not-finished'),
]