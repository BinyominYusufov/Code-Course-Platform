from django.urls import path
from .views import *
urlpatterns = [
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>/', CourseDetailView.as_view()),
    path('courses/create/', CourseCreateView.as_view()),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view()),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view()),


    path('modules/', ModuleListView.as_view()),
    path('modules/<int:pk>/', ModuleDetailView.as_view()),
    path('modules/create/', ModuleCreateView.as_view()),
    path('modules/<int:pk>/update/', ModuleUpdateView.as_view()),
    path('modules/<int:pk>/delete/', ModuleDeleteView.as_view()),


    path('tasks/', TaskListView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('tasks/create/', TaskCreateView.as_view()),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view()),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view()),

]
