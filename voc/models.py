from django.db import models

def get_upload_path(instance, filename):
    return 'voc/{}'.format(filename)

class Voc(models.Model):
     title = models.CharField(max_length=200)
     content = models.TextField()
     image = models.ImageField(
          upload_to=get_upload_path, default=None)
     email = models.CharField(max_length=100, blank=True, null=False)


# Create your models here.
