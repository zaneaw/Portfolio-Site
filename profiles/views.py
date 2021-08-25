from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import CreateView, DetailView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User, UserManager
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm

User = get_user_model()

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')
    

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.User

    def form_valid(self, form):
        form.save()
        return redirect('accounts:view_profile', self.object.username)


class ViewProfileView(DetailView):
    model = User
    template_name = 'registration/view_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        ctx = super(ViewProfileView, self).get_context_data(*args, **kwargs)

        page_profile = get_object_or_404(Profile, id=self.kwargs['pk'])

        ctx['page_profile'] = page_profile
        return ctx
        
    def get_object(self):
        username = self.kwargs.get("username")
        return get_object_or_404(User, username=username)


def password_success(request):
    return render(request, 'registration/password_success.html', {})
