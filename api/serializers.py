from rest_framework import serializers
from .models import Task
from datetime import datetime


class TaskSerializer(serializers.Serializer):
    id          = serializers.IntegerField(read_only=True)
    title       = serializers.CharField(max_length=200)
    completed   = serializers.BooleanField(default=False)
    description = serializers.CharField(default='', allow_blank=True)
    created     = serializers.DateTimeField(default=datetime.now)

    def to_representation(self, instance: Task): 
        return {
            "info": f"{instance.id}. {instance.title} is {'completed' if instance.completed else 'not completed'}."
        }

    def create(self, validated_data: dict) -> Task:
        return Task.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            completed=validated_data['completed']
        )
