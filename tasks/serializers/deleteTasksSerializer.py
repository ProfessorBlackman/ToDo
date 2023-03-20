from rest_framework import serializers


# serializer for DeleteTasks view
class DeleteTasksSerializer(serializers.Serializer):
    id = serializers.IntegerField()
