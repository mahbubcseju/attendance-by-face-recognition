from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField('Course Name', max_length=128)
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_all_students_info(self):
        students = self.coursestudent_set.all()
        return students

    def get_joined_students_info(self):
        students = self.coursestudent_set.filter(status__lte=1)
        return students

    def get_recent_periods(self):
        periods = self.attendanceperiod_set.all().order_by('-start_at')[:10]
        return periods


class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
