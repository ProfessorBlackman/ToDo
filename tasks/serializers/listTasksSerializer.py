from rest_framework import serializers
from ..models import TasksData


# serializer for ListTasks view
class ListTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksData
        fields = "__all__"
