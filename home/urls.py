from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('detail/<int:todo_id>/', views.detail, name = 'detail'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('create/', views.CreateTodo, name='create'),
    path('register/', views.UserRegister, name='register'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
]