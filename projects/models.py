
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.conf import settings

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30, validators=[MinLengthValidator(2, "Must be more than 2 characters."), MaxLengthValidator(30, "Must be less than 30 characters.")])
    desc = models.TextField()
    repo = models.URLField(blank=True)
    image = models.BinaryField(null=True, blank=True, editable=True)    
    content_type = models.CharField(max_length=256, null=True, blank=True, 
                                    help_text='The MIMEType of the file')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # This is what shows up in the admin list
    def __str__(self):
        return f"{self.title} - {self.owner}"