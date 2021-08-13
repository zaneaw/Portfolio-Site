from django.http.response import HttpResponse
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from projects.forms import ProjectCreateForm, ProjectUpdateForm
from projects.models import Project


class ProjectListView(OwnerListView):
    model = Project
    template_name = 'projects/project_list.html'
    ordering = ['-pk']


class ProjectDetailView(OwnerDetailView):
    model = Project
    template_name = 'projects/project_detail.html'


class ProjectCreateView(LoginRequiredMixin, FormView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('projects:all')
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed
        # It should return an HttpResponse
        form.send_email()
        return super().form_valid(form)

    def post(self, request, pk=None):
        form = ProjectCreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to model before save
        project = form.save(commit=False)
        project.owner = self.request.user
        project.save()
        return redirect(self.success_url)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'projects/project_update.html'
    # fields = ['title', 'desc', 'repo', 'image']
    success_url = reverse_lazy('projects:all')


class ProjectDeleteView(OwnerDeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('projects:all')


