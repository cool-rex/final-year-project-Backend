from django.shortcuts import render
from .models import Course, CoursePastQuestion
from .serializers import CourseSerializer, CoursePastQuestionSerializer, CoursePastQuestionSerializer1
from rest_framework import generics

# Create your views here.


# This view is to handle both listing coures and creating new courses
# queryset retrieves all courses by id
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all().order_by('course_id')
    serializer_class = CourseSerializer


# for mannuplating courses(retrieving course, updating and deleting
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


#similar to CourseList view but for past questions
class CoursePastQuestionList(generics.ListCreateAPIView):
    queryset = CoursePastQuestion.objects.all().order_by('-id')
    serializer_class = CoursePastQuestionSerializer


# for mannuplating Pastquestion(retrieving pastquestions, updating and deleting

class CoursePastQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoursePastQuestion.objects.all()
    serializer_class = CoursePastQuestionSerializer

class CoursePastQuestionList1(generics.ListCreateAPIView):
    queryset = CoursePastQuestion.objects.all().order_by('-id')
    serializer_class = CoursePastQuestionSerializer1


# This view lists all the past questions for a specific course
# # It uses the courseid to filter the past questions by the associated course
class CourseToCoursePastQuestion(generics.ListAPIView):
    serializer_class = CoursePastQuestionSerializer1

    def get_queryset(self):
        course_id=self.kwargs['course_id']
        course = Course.objects.get(pk=course_id)
        return CoursePastQuestion.objects.filter(course=course).order_by('-id')