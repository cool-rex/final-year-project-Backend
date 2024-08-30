from rest_framework import serializers
from .models import Course, CoursePastQuestion

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'course_id',
            'course_title',
        )
        model = Course

class CoursePastQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'course',
            'title',
            'pastQuestionFile',
        )
        model = CoursePastQuestion

class CoursePastQuestionSerializer1(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'course',
            'title',
            'pastQuestionFile',
        )
        model = CoursePastQuestion
        depth = 1