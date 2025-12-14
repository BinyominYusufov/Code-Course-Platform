from rest_framework import serializers
from .models import Task,CourseModule,Course

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['module','title','description','max_score','is_active','created_at']



class ModuleSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = CourseModule
        fields = ['course','title','order','tasks']


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id','title','description','is_active','created_at','modules']



