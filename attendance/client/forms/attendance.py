from django import forms

from database.models import AttendancePeriod


class InitializeAttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendancePeriod
        fields = (
            'period',
        )
