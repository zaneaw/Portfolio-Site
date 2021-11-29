from django.urls import path, reverse_lazy
from . import views

app_name='projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='all'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/comment', views.CommentCreateView.as_view(), name='project_comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(success_url=reverse_lazy('projects')), name='project_comment_delete'),
    path('project_create', views.ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/update', views.ProjectUpdateView.as_view(), name='project_update'),
    path('<int:pk>/delete', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('<int:pk>/like', views.ProjectLikeView, name='project_like'),
    # path('jarvis')
]


# I use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
