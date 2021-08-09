from django import forms
from .models import Project
from django.core.files.uploadedfile import InMemoryUploadedFile
from .humanize import naturalsize

class ProjectCreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    """Form for the image model"""

    image = forms.FileField(required=False, label='File to Upload <= ' + max_upload_limit_text)
    upload_field_name = 'image'
    class Meta:
        model = Project
        fields = ['title', 'desc', 'repo', 'image']
        labels = {'title': 'Title', 'desc': 'Description', 'repo': 'Repository Link', 'image': 'Image'}

    # Validate pic size
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < " + self.max_upload_limit_text + " bytes")

    # Convert uploaded file to a pic
    def save(self, commit=True):
        instance = super(ProjectCreateForm, self).save(commit=False)

        # We only need to adjust pic if it is freshly uploaded
        f = instance.image # Makes a copy
        if isinstance(f, InMemoryUploadedFile): # Extracts data from form to model
            bytearray = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearray

        if commit:
            instance.save()

        return instance
        

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
