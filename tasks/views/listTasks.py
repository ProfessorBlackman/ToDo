from django.http import HttpResponseRedirect
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import TasksData
# from tasks.serializers.listTasksSerializer import ListTasksSerializer
from ..serializers.listTasksSerializer import ListTasksSerializer


#  view for displaying all tasks
class ListTasksView(generics.ListAPIView):
    serializer_class = ListTasksSerializer

    @swagger_auto_schema(operation_summary='list all tasks')
    def get_queryset(self):
        try:
            tasks = TasksData.objects.all()
            print(tasks)
            return tasks
        except:
            response = {
                'status': 'failure',
                'error': 'unable to get objects'
            }
            return Response(data=response, status=status.HTTP_404_NOT_FOUND)
