from django import forms
from .models import Project
from django.core.files.uploadedfile import InMemoryUploadedFile
from .humanize import naturalsize

class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'desc', 'repo', 'image']
        labels = {'title': 'Title', 'desc': 'Description', 'repo': 'Repository Link', 'image': 'Image', 'owner': 'Created by'}
        

# class ProjectUpdateForm(forms.ModelForm):

#     class Meta:
#         model = Project
#         fields = ['title', 'desc', 'repo', 'image']
#         labels = {'title': 'Title', 'desc': 'Description', 'repo': 'Repository Link', 'image': 'Image', 'owner': 'Created by'}

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
