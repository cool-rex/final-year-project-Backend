from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=10, null=False, primary_key=True)
    course_title = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.course_id
    
class CoursePastQuestion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False)
    pastQuestionFile = models.FileField(null=True)

    def __str__(self):
        return self.title