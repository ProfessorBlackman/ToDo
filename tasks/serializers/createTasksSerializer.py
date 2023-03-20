from rest_framework import serializers

from ..models import TasksData


# serializer for creating a new task in the CreateTasks view
class CreateTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksData
        fields = ['title', 'about']
    # title = serializers.CharField(max_length=100)
    # about = serializers.CharField(max_length=300)
