from rest_framework import serializers
from .models import Course, CoursePastQuestion


#  validate incoming data when creating or updating a course.
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'course_id',
            'course_title',
        )
        model = Course


# handle validation for operations like creation or update.
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