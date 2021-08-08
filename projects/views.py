
from projects.models import Project
from projects.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class ProjectListView(OwnerListView):
    model = Project


class ProjectDetailView(OwnerDetailView):
    model = Project


class ProjectCreateView(OwnerCreateView):
    model = Project


class ProjectUpdateView(OwnerUpdateView):
    model = Project



def project_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'projects': project}
    return render(request, 'project_detail.html', context)

