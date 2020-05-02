from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from client.forms import InitializeAttendanceForm
from database.models import Course, AttendancePeriod


class InitializeAttendance(FormView):
    template_name = 'client/initialize_attendance.html'
    form_class = InitializeAttendanceForm

    def post(self, request, course_id, *args, **kwargs):
        form = self.form_class(request.POST)
        self.course_id = course_id

        if form.is_valid():
            course = Course.objects.get(id=course_id)
            obj = form.save(commit=False)
            obj.course = course
            obj.save()
            return self.form_valid(form)

        return self.form_invalid(form)

    def get_success_url(self):
        self.request.session['start-attendance'] = True
        return reverse_lazy(
            'CourseDetail',
            kwargs={'pk': self.course_id }
        )


class ProcessAttendance(TemplateView):
    template_name = 'client/process_attendance.html'

    def dispatch(self, request, period_id, *args, **kwargs):
        self._period = AttendancePeriod.objects.get(id=period_id)
        return super().dispatch(request, period_id, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['period'] = self._period
        return context
