
from django.urls import path
from .views import home_view, auth_view, logout_view, update_view, delete_task, toggle_view

urlpatterns = [
    path('', home_view, name='home'),
    path('auth/', auth_view, name = 'auth'),
    path('logout/', logout_view, name='logout'),
    path('update/<int:taskid>/', update_view, name='update'),
    path('delete/<int:task_id>', delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', toggle_view, name='toggle_task')
]
