from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile") 
    social_fb = models.CharField(max_length=255, null=True, blank=True)
    social_tw = models.CharField(max_length=255, null=True, blank=True) 
    social_insta = models.CharField(max_length=255, null=True, blank=True) 
    social_lin = models.CharField(max_length=255, null=True, blank=True)
    social_git = models.CharField(max_length=255, null=True, blank=True) 


    def __str__(self):
        return str(self.user)