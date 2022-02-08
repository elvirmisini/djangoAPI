from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100)
    # date =serializers.DateTimeField()
    #
    # def create(self, validated_data):
    #     return Task.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title=validated_data.get('title',instance.title)
    #     instance.date=validated_data.get('date',instance.date)
    #     instance.save()
    #     return instance

    class Meta:
        model=Task
        fields=['id','title','date']