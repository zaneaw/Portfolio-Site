from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')
    

class EditProfileView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect('accounts:view_profile', self.object.username)


class ViewProfileView(generic.DetailView):
    template_name = 'registration/view_profile.html'
    queryset = User.objects.all()

    def get_object(self):
        username = self.kwargs.get("username")
        return get_object_or_404(User, username=username)


def password_success(request):
    return render(request, 'registration/password_success.html', {})
