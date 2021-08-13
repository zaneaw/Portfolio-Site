from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30, validators=[MinLengthValidator(2, "Must be more than 2 characters."), MaxLengthValidator(30, "Must be less than 30 characters.")])
    desc = models.TextField()
    repo = models.URLField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/", default='images/filler_project_image.jpg')    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # This is what shows up in the admin list
    def __str__(self):
        return f"{self.title} - {self.owner}"
