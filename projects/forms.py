from django import forms
from .models import Project
from django.core.files.uploadedfile import InMemoryUploadedFile
from .humanize import naturalsize

class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'desc', 'repo', 'image')
        labels = {'title': 'Title', 'desc': 'Description', 'repo': 'Repository Link', 'image': 'Image', 'owner': 'Created by'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'repo': forms.TextInput(attrs={'class': 'form-control'}), # Go back to - https://youtu.be/6-XXvUENY_8?t=738
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
        

class ProjectUpdateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'desc', 'repo', 'image']
        labels = {'title': 'Title', 'desc': 'Description', 'repo': 'Repository Link', 'image': 'Image', 'owner': 'Created by'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'repo': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
        }

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
