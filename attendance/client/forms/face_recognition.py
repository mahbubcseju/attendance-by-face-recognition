from django import forms

from database.models import FaceImageBase

class RegisterImageForm(forms.ModelForm):
    class Meta:
        model = FaceImageBase
        fields = ['image']
