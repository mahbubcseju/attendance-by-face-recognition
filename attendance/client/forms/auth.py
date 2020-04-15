from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    use_required_attribute = False

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


class LoginForm(forms.Form):

    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
    )
