from django.db import models

# Create your models here.
class Project(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    abstract    = models.TextField(default='SOME STRING')
    technology  = models.CharField(max_length=20)
    image       = models.FilePathField(path="/static")

    def __str__(self):
        return self.title