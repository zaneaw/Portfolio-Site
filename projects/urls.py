from django.urls import path, reverse_lazy
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectLikeView

app_name='projects'
urlpatterns = [
    path('', ProjectListView.as_view(), name='all'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project_create', ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),
    path('<int:pk>/like', ProjectLikeView, name='project_like'),
]


# I use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
