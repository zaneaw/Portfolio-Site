from django.contrib.auth import login, authenticate
from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import SignUpForm

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def signup(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
        else:
            form = SignUpForm()
        return render