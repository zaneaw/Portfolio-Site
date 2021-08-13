from django.http.response import HttpResponse
from django.views import View, generic
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from projects.forms import ProjectCreateForm
from projects.models import Project


class ProjectListView(OwnerListView):
    model = Project
    template_name = 'projects/project_list.html'


class ProjectDetailView(OwnerDetailView):
    model = Project
    template_name = 'projects/project_detail.html'


class ProjectCreateView(LoginRequiredMixin, View):
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('projects:all')
    
    def get(self, request, pk=None):
        form = ProjectCreateForm
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

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


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    fields = ['title', 'desc', 'repo', 'image']
    success_url = reverse_lazy('projects:all')


class ProjectDeleteView(OwnerDeleteView):
    model = Project
    template_name = 'projects/project_delete.html'

