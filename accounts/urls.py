from django.urls import path
from .views import add_view, check_task_status

urlpatterns = [
    path('add/', add_view, name='add_view'),
    path('task_status/<str:task_id>/', check_task_status, name='check_task_status'),
]
