from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class PasswordChangeView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'


class PasswordChangeDoneView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/password_change_done.html'


class PasswordResetView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:password_reset_done')
    template_name = 'users/password_reset_form.html'


class PasswordResetDoneView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('user:password_reset_complete')
    template_name = 'users/password_reset_confirm.html'


class PasswordResetCompleteView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/password_reset_complete.html'
