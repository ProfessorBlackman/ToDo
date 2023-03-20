from django.urls import path

from .views.createTasks import CreateTasks
from .views.listTasks import ListTasksView
from .views.DeleteTasks import DeleteTasks
from .views.completeTask import CompleteTasks
from .views.updateTasks import UpdateTasks

app_name = 'urlShortener'


urlpatterns = [

    path('create/', CreateTasks.as_view(), name='create tasks'),
    path('complete/', CompleteTasks.as_view(), name='complete tasks'),
    path('delete/', DeleteTasks.as_view(), name='delete tasks'),
    path('list/', ListTasksView.as_view(), name='list tasks'),
    path('update/', UpdateTasks.as_view(), name='update tasks'),
]