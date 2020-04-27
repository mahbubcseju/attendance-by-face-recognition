import json

from django.views.generic import DetailView, View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.http import HttpResponse

from database.models import Course, CourseStudent


@method_decorator(login_required, name='dispatch')
class CourseDetail(DetailView):
    model = Course
    slug_id=id
    template_name = 'client/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class APIStudentInvite(View):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('name')
        course_id = request.POST.get('course_id')

        try:
            user = User.objects.get(username=username)
            course = Course.objects.get(id=course_id)
            is_duplicate_exit = CourseStudent.objects.filter(user=user, course=course).count()
            if is_duplicate_exit:
                obj = {
                    'status': 'NG',
                    'result': 'Already invitation sent to this user.',
                }
            else:
                CourseStudent.objects.create(user=user, course=course)
                self.request.session['student-added'] = True
                obj = {
                    'status': 'OK',
                    'result': reverse('CourseDetail', kwargs={'pk': course.id})
                }
        except Exception as e:
            obj = {
                'status': 'NG',
                'result': 'Creation failed. Try Again.',
            }

        res = HttpResponse(
            json.dumps(obj, ensure_ascii=False, indent=2),
            content_type='application/json',
        )
        if obj['status'] == 'NG':
            res.status_code = 500
        return res
