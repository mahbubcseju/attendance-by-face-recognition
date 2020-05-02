import json

from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.http import HttpResponse

from database.models import (
    Course,
    CourseStudent,
    AttendancePeriod,
)


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'client/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        my_courses = CourseStudent.objects.filter(user=self.request.user)
        my_courses = [entry.course for entry in my_courses]
        my_periods = AttendancePeriod.objects.filter(course__in=my_courses)
        my_active_periods = [
            period for period in my_periods if timezone.now() <= (
                    period.start_at + timezone.timedelta(minutes=period.period)
            )
        ]

        context['supervised_courses'] = Course.objects.filter(supervisor=self.request.user)
        context['student_courses'] = CourseStudent.objects.filter(user=self.request.user)
        context['active_periods'] = my_active_periods
        print(context['active_periods'])
        return context


@method_decorator(login_required, name='dispatch')
class APICourseCreate(View):

    def post(self, request, *args, **kwargs):
        course_name = request.POST.get('name')
        try:
            course = Course.objects.create(name=course_name, user=request.user)
            self.request.session['course-added'] = True
            obj = {
                'status': 'OK',
                'result': reverse('Home')
            }
        except Exception:
            obj = {
                'status': 'NG',
                'result': 'Saved failed',
            }

        res = HttpResponse(
            json.dumps(obj, ensure_ascii=False, indent=2),
            content_type='application/json',
        )
        if obj['status'] == 'NG':
            res.status_code = 500
        return res


@method_decorator(login_required, name='dispatch')
class APIInvitationUpdate(View):

    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        status = request.POST.get('status')
        try:
            entry = CourseStudent.objects.get(id=id)
            entry.status = status
            entry.save()
            self.request.session['invitation-updated'] = True
            obj = {
                'status': 'OK',
                'result': reverse('Home')
            }
        except Exception:
            obj = {
                'status': 'NG',
                'result': 'Saved failed',
            }

        res = HttpResponse(
            json.dumps(obj, ensure_ascii=False, indent=2),
            content_type='application/json',
        )
        if obj['status'] == 'NG':
            res.status_code = 500
        return res
