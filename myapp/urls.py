from django.urls import path
from .import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]