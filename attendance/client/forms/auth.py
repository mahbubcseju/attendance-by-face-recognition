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

    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={'size': 40}),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Required. Inform a valid email address.'
    )
    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'size': 40}),
    )
    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={'size': 40}),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput(),
    )


class LoginForm(forms.Form):

    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
    )
