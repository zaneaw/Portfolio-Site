from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import FileResponse
import os

from projects.owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from projects.forms import ProjectCreateForm, ProjectUpdateForm, CommentForm
from projects.models import Project, Comment


class ProjectListView(OwnerListView):
    model = Project
    template_name = 'projects/project_list.html'


class ProjectDetailView(OwnerDetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get(self, request, pk):
        p = Project.objects.get(id=pk)
        comments = Comment.objects.filter(project=p).order_by('-date_updated')
        comment_form = CommentForm()
        total_likes = p.total_likes()
        liked = False
        if p.likes.filter(id=self.request.user.id).exists():
            liked = True
        ctx = {'project': p, 'total_likes': total_likes, 'liked': liked, 'comment_form': comment_form, 'comments': comments}
        return render(request, self.template_name, ctx)


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
        ctx = {'form': form}
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to model before save
        project = form.save(commit=False)
        project.owner = self.request.user
        project.save()
        return redirect('projects:project_detail', project.pk)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'projects/project_update.html'
    
    def get(self, request, pk):
        project_inst = get_object_or_404(Project, id=pk, owner=self.request.user)
        form = ProjectCreateForm(instance=project_inst)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk = None, *args, **kwargs):
        self.object = self.get_object() # assign the object to the
        project_inst = get_object_or_404(Project, id=pk, owner=self.request.user)
        form = ProjectCreateForm(request.POST, request.FILES or None, instance=project_inst)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        project = form.save(commit=False)
        project.save()

        return redirect('projects:project_detail', self.object.pk)

    def form_valid(self, form):
        return redirect('projects:project_detail', self.object.pk)


class ProjectDeleteView(OwnerDeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('projects:all')


def ProjectLikeView(request, pk):
    project = get_object_or_404(Project, id=request.POST.get('project_pk'))
    liked = False # Default value
    if project.likes.filter(id=request.user.id).exists():
        project.likes.remove(request.user)
        liked = False
    else:
        project.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('projects:project_detail', args=[str(pk)]))
    # 'request' contains the users ID if logged in when clicking 'like'.
    # project.likes.filter(id=request.user.id) then looks at the current 
    # project's likes and filters them to show if the current user id has 
    # liked the current project. If it exists, it 'removes' the like. If 
    # it doesn't, it adds the like to the DB\
    # This code then is passed into the ProjectDetailView


class CommentCreateView(LoginRequiredMixin, View):
    model = Comment
    template_name = 'projects/project_comment_create.html'

    def post(self, request, pk):
        p = get_object_or_404(Project, id=pk)
        comment = Comment(
            text=request.POST['comment'], owner=request.user, project=p)
        comment.save()
        return redirect(reverse('projects:project_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = 'projects/project_comment_delete.html'

    def get_success_url(self):
        project = self.object.project
        return reverse('projects:project_detail', args=[project.id])