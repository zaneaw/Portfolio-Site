from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField


def file_size(value):
    limit = 2621440 # 2.5 * 1024 * 1024, or 2.5MB
    if value.size > limit:
        raise ValidationError('File size is too large. Size should not exceed 2.5MB')


class Project(models.Model):
    title = models.CharField(max_length=30, validators=[MinLengthValidator(2, "Must be more than 2 characters."), MaxLengthValidator(30, "Must be less than 30 characters.")])
    desc = RichTextField(blank=True, null=True)
    repo = models.URLField(blank=True)
    image = models.ImageField(null=True, blank=True, validators=[file_size], upload_to="media/")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_projects')


    def total_likes(self):
        return self.likes.count()
        
    # This is what shows up in the admin list
    def __str__(self):
        return f"{self.title} - {self.owner}"


class Comment(models.Model):
    project = models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(validators=[MinLengthValidator(3, "Comments must be more than 2 characters")])
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.text) < 15:
            return self.text
        return self.text + '...'

