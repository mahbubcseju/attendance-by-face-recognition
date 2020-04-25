from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField('Course Name', max_length=128)


class CourseStudent(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
