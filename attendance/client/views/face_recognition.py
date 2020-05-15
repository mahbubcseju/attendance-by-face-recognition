import re
import base64
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView
from django.utils.decorators import method_decorator
from django.core.files.base import ContentFile

from client import forms
from database.models import FaceImageBase


@method_decorator(login_required, name='dispatch')
class RegisterImage(TemplateView):
    template_name = 'client/register_image.html'

    def post(self, request, username, *args, **kwargs):
        try:
            imageData = request.POST.get('image')
            dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
            imageData = dataUrlPattern.match(imageData).group(2)
            file = base64.b64decode(imageData)
            image = ContentFile(file, '{}.jpeg'.format(username))
            current_image = FaceImageBase.objects.filter(user=request.user)
            if current_image:
                obj = FaceImageBase.objects.filter(user=request.user)
                obj.image = image
                obj.save()
            else:
                FaceImageBase.objects.filter(user=request.user, image=image)
            obj = {
                'status': 'OK',
                'result': reverse('Home'),
            }
        except Exception as e:
            obj = {
                'status': 'NG',
                'result': str(e),
            }

        res = HttpResponse(
            json.dumps(obj, ensure_ascii=False, indent=2),
            content_type='application/json',
        )
        if obj['status'] == 'NG':
            res.status_code = 500
        return res
