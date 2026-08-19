from django.urls import path
from todo.views import dashboard
from . import views

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('api/todos/', views.todo_list_create_api, name='todo_list_create_api'),
    path('api/todos/<int:pk>/', views.todo_detail_update_delete_api, name='todo_detail_update_delete_api'),
]
