from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from ckeditor.fields import RichTextField


def file_size(value):
    limit = 2621440 # 2.5 * 1024 * 1024, or 2.5MB
    if value.size > limit:
        raise ValidationError('File size is too large. Size should not exceed 2.5MB')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about = RichTextField(blank=True, null=True, max_length=1000) 
    profile_pic = models.ImageField(null=True, blank=True, validators=[file_size], upload_to="media/")
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)