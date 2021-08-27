from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.encoding import force_text


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, db_index=True, unique=True)
    about = models.TextField(max_length=500, null=True, blank=True) 
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.user.username
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)