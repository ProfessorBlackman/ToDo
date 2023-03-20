from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from datetime import datetime

from ..models import TasksData

# from ..serializers.completeTasksSerializer import CompleteTasksSerializer
from ..serializers.completeTaskSerializer import CompleteTasksSerializer


# view for marking a task as complete
class CompleteTasks(generics.GenericAPIView):
    serializer_class = CompleteTasksSerializer

    # This function deletes a task
    @swagger_auto_schema(operation_summary='Complete a task')
    def post(self, request, *args, **kwargs):
        data = request.data
        task_id = data.get('id')
        print(task_id)

        try:
            task = TasksData.objects.get(id=task_id)
            print(task)
            task.isCompleted = True
            task.save()
            new = TasksData.objects.get(id=task_id)
            print(new)
        except:
            response = {
                'status': 'error',
                'error': f"task with id: {task_id} does not exist"
            }
            return Response(data=response, status=status.HTTP_404_NOT_FOUND)



        response = {
            'status': 'success',
            'data': 'task completed'
        }
        return Response(data=response, status=status.HTTP_200_OK)
