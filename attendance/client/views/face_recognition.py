import re
import base64

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.utils.decorators import method_decorator
from django.core.files.base import ContentFile

from client import forms
from database.models import FaceImageBase


@method_decorator(login_required, name='dispatch')
class RegisterImage(FormView):
    template_name = 'client/register_image.html'
    success_url = reverse_lazy('Home')
    form_class = forms.RegisterImageForm

    def post(self, request, username, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            image = ContentFile(form.cleaned_data['image'].read(), '{}.jpeg'.format(username))
            FaceImageBase.objects.create(user=request.user, image=image)
            return self.form_valid(form)
        return self.form_invalid(form)
