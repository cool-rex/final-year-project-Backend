from django.contrib import admin
from .models import Course, CoursePastQuestion

# Register your models here.

admin.site.register(Course)
admin.site.register(CoursePastQuestion)