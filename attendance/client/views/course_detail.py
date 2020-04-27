from django.views.generic import DetailView
from django.contrib.auth.models import User

from database.models import Course



class CourseDetail(DetailView):
    model = Course
    slug_id=id
    template_name = 'client/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
