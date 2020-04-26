from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField('Course Name', max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
