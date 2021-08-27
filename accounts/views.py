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
from .forms import SignUpForm, EditUserForm, EditProfileForm, ChangePasswordForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    

class EditUserView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'registration/edit_user.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

    def form_valid(self, form):
        form.save()
        return redirect('accounts:view_profile', self.object.profile.id)


class ViewProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/view_profile.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

# https://stackoverflow.com/questions/68956898/return-specific-user-in-django/68956946?noredirect=1#comment121867879_68956946


class EditProfileView(LoginRequiredMixin ,generic.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        form.save()
        return redirect('accounts:view_profile', self.object.user.username)



class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})
