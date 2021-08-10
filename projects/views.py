
from django.http.response import HttpResponse
from django.views import View
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
    template_name = 'projects/project_form.html'
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


class ProjectUpdateView(LoginRequiredMixin, View):
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:all')

    def get(self, request, pk):
        image = get_object_or_404(Project, id=pk, owner=self.request.user)
        form = ProjectCreateForm(instance=image)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        image = get_object_or_404(Project, id=pk, owner=self.request.user)
        form = ProjectCreateForm(request.POST, request.FILES or None, instance=image)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        image = form.save(commit=False)
        image.save()

        return redirect(self.success_url)

class ProjectDeleteView(OwnerDeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'


def stream_file(request, pk):
    image = get_object_or_404(Project, id=pk)
    response = HttpResponse()
    response['Content-Type'] = image.content_type
    response['Content-Length'] = len(image.image)
    response.write(image.image)
    return response



