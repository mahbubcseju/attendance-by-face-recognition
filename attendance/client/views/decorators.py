from django.shortcuts import redirect
from django.urls import reverse_lazy

from database.models import FaceImageBase


def face_image_uploaded(function):
    def _function(request, *args, **kwargs):
        user = request.user
        try:
            FaceImageBase.objects.get(user=user)
        except Exception:
            return redirect(reverse_lazy('LogOut'))
        return function(request, *args, **kwargs)
    return _function
