from django.urls import path
from .views import task_list,task_detail,task_delete,task_today,task_update,front,report,AddTask,EditTask,DeleteTask

urlpatterns = [
    path('task/', task_list),
    path('task/<int:pk>/',task_detail),
    path('task/<int:pk>/delete/', task_delete),
    path('task/<int:pk>/update/', task_update),
    path('task/today/', task_today,),
    path('report/', report),
    path('add/', AddTask,name='AddTask'),
    path('edit/<int:pk>/edit', EditTask, name='EditTask'),
    path('delete/<int:pk>/delete', DeleteTask, name='DeleteTask'),
    path('', front,name='home'),
]