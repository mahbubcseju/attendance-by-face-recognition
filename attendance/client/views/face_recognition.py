from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.utils.decorators import method_decorator

from client import forms


@method_decorator(login_required, name='dispatch')
class RegisterImage(FormView):
    template_name = 'client/register_image.html'
    form_class = forms.RegisterImageForm
    success_url = reverse_lazy('Home')

    # def post(self, request, username, *args, **kwargs):

