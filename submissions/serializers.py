from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['user','task','answer','score','status','created_at','updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['username'] = instance.user.username
        data['course'] = instance.task.module.course.title
        data['module'] = instance.task.module.title
        data['task'] = instance.task.title

        return data
    
    def validate_score(self, value):
        task = self.instance.task if self.instance else self.initial_data.get('task')
        max_score = task.max_score if hasattr(task, 'max_score') else None
        if value > max_score:
            raise serializers.ValidationError("Score cannot exceed max_score")
        return value

    def validate(self, attrs):
        task = attrs.get('task')
        if not task.is_active:
            raise serializers.ValidationError("Cannot submit inactive task")
        return attrs    
