from django.contrib import admin

from .models import (
    AttendancePeriod,
    AttendanceEntry,
    Course,
    CourseStudent,
    FaceImageBase,
)

admin.site.register(AttendancePeriod)
admin.site.register(AttendanceEntry)
admin.site.register(Course)
admin.site.register(CourseStudent)
admin.site.register(FaceImageBase)
