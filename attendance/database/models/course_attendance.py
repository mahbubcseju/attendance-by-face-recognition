from django.db import models
from django.utils import timezone
from .courses import Course, CourseStudent


class AttendancePeriod(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_at = models.DateTimeField('Start at', default=timezone.now)
    period = models.IntegerField('Period', default=45)
    date = models.DateField('Date', default=timezone.now)

    def get_remaining_time(self):
        remaining_time = self.start_at + timezone.timedelta(minutes=self.period) - timezone.now()
        seconds = remaining_time.total_seconds()
        minutes = seconds // 60
        return minutes


class AttendanceEntry(models.Model):
    period = models.ForeignKey(AttendancePeriod, on_delete=models.CASCADE)
    course_student = models.ForeignKey(CourseStudent, on_delete=models.CASCADE)
