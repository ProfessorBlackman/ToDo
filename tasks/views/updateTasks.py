from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from datetime import datetime

from ..models import TasksData

# from tasks.serializers.updateTasksSerializer import UpdateTasksSerializer
from ..serializers.updateTasksSerializer import UpdateTasksSerializer


#  view to update a task
class UpdateTasks(generics.GenericAPIView):
    serializer_class = UpdateTasksSerializer

    # This function updates a task
    @swagger_auto_schema(operation_summary='Update a task')
    def post(self, request, *args, **kwargs):
        data = request.data
        task_id = data.get('id')
        title = data.get('title')
        about = data.get('about')
        if len(title) != 0 and len(task_id) != 0:
            if TasksData.objects.filter(title=title).exists():
                response = {
                    'status': 'error',
                    'error': "task already exists"
                }
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
            else:
                task = TasksData.objects.get(id=task_id)
                print(task)
                task.title = title
                print(title)
                if len(about) != 0:
                    task.about = about
                    print(about)
                task.save()

            response = {
                'status': 'success',
                'data': f'task no: {task_id} updated'
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            response = {
                'status': 'error',
                'error': "You need to input a title"
            }
            return Response(data=response, status=status.HTTP_204_NO_CONTENT)
