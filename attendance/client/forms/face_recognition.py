from django import forms


class RegisterImageForm(forms.Form):
    image = forms.FileField()
