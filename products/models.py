
# Create your models here.
from django.db import models
from datetime import datetime

def get_upload_path(instance, filename):
    return 'products/{}'.format(filename)

class Product(models.Model):
     title = models.CharField(max_length=200)
     content = models.TextField()
     popularity = models.IntegerField(default=0)
     pub_date = models.DateTimeField('date published',default=datetime.now)
     image = models.ImageField(
          upload_to=get_upload_path, default='place_image.png')
