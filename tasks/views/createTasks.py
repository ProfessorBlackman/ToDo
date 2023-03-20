from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

# from tasks.serializers.addTasksSerializer import CreateTasksSerializer
from ..serializers.createTasksSerializer import CreateTasksSerializer
from ..models import TasksData


#  view for displaying all tasks
class CreateTasks(generics.GenericAPIView):
    serializer_class = CreateTasksSerializer

    @swagger_auto_schema(operation_summary='create new tasks')
    def post(self, request, *args, **kwargs):
        data = request.data
        # title = data.get('title')
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {
                'status': 'success',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            response = {
                'status': 'error',
                'errors': serializer.errors
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
