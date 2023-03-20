from datetime import datetime
from rest_framework import serializers
from ..models import TasksData


# serializer for CompleteTasks view
class CompleteTasksSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # completed_at = serializers.CharField()
    class Meta:
        model = TasksData
        fields = ["id", "isCompleted", "date_completed"]
