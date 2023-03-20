from rest_framework import serializers
from datetime import datetime
from ..models import TasksData


# serializer for the UpdateTasks view
class UpdateTasksSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=100, required=True)
    # about = serializers.CharField(max_length=300)
    # # updated_at = serializers.CharField()
    class Meta:
        model = TasksData
        fields = ["id", "title", "about", "update_at"]
