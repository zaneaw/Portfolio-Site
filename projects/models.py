from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=40)
    desc = models.TextField()
    repo = models.URLField(blank=True)
    image = models.FilePathField(path='/img')

    def __str__(self):
        return self.title + ' - ' + self.repo