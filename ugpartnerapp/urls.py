from django.urls import path
from .views import CourseList, CourseDetail, CoursePastQuestionList, CoursePastQuestionDetail, CoursePastQuestionList1, CourseToCoursePastQuestion

urlpatterns = [
    path('', CourseList.as_view()),
    path('<str:pk>', CourseDetail.as_view()),
    path('course-past-question/', CoursePastQuestionList.as_view()),
    path('course-past-question-list/', CoursePastQuestionList1.as_view()),
    path('course-past-question/<str:pk>', CoursePastQuestionDetail.as_view()),
    path('course-to-course-past-question/<str:course_id>', CourseToCoursePastQuestion.as_view()),
]