import json

from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.http import HttpResponse

from database.models import Course, CourseStudent


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'client/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['supervised_courses'] = Course.objects.filter(supervisor=self.request.user)
        context['student_courses'] = CourseStudent.objects.filter(user=self.request.user)
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
