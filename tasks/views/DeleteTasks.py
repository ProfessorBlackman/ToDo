from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from datetime import datetime

from tasks.models import TasksData

# from tasks.serializers.deleteTasksSerializer import DeleteTasksSerializer
from ..serializers.deleteTasksSerializer import DeleteTasksSerializer


# view for deleting a task
class DeleteTasks(generics.DestroyAPIView):
    serializer_class = DeleteTasksSerializer

    # This function deletes a task
    @swagger_auto_schema(operation_summary='Delete a task')
    def post(self, request, *args, **kwargs):
        data = request.data
        task_id = data.get('id')
        if TasksData.objects.filter(id=task_id).exists():
            task = TasksData.objects.get(id=task_id)
            task.delete()
        else:
            response = {
                'status': 'error',
                'error': f"task with id: {task_id} does not exist"
            }
            return Response(data=response, status=status.HTTP_404_NOT_FOUND)
        response = {
            'status': 'success',
            'data': 'task deleted'
        }
        return Response(data=response, status=status.HTTP_200_OK)
