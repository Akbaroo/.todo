from django.urls import path

from .views import TodoView, TodoDetailView

app_name = 'todo'

urlpatterns = [
    path('', TodoView.as_view(), name='todo'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]