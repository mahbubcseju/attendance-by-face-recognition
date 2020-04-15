from django.db import transaction
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    FormView,
    TemplateView,
    View,
)

from client import forms


class SignUp(FormView):
    form_class = forms.SignUpForm
    template_name = 'client/sign_up.html'

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return self.form_valid(form)

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('SignUpDone')


class SignUpDone(TemplateView):
    template_name = 'client/sign_up_done.html'


class Login(FormView):
    template_name = 'client/login.html'
    form_class = forms.LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)

            if user:
                login(request, user)
                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return self.form_valid(form)

            return self.form_invalid(form)

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('Home')


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('Home'))
