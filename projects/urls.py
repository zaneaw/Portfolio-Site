from django.urls import path, reverse_lazy
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

app_name='projects'
urlpatterns = [
    path('', ProjectListView.as_view(), name='all'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project_create', ProjectCreateView.as_view(success_url=reverse_lazy('projects:all')), name='project_create'),
    path('<int:pk>/update', ProjectUpdateView.as_view(success_url=reverse_lazy('projects:all')), name='project_update'),
    path('<int:pk>/delete', ProjectDeleteView.as_view(success_url=reverse_lazy('projects:all')), name='project_delete'),
]


# I use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
