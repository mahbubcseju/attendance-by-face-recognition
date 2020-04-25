from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(label='Course Name')


class CourseStudent(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
