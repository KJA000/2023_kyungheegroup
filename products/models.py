
# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


def get_upload_path(instance, filename):
    return 'products/{}'.format(filename)

class Product(models.Model):
     title = models.CharField(max_length=200)
     content = models.TextField()
     popularity = models.IntegerField(default=0)
     pub_date = models.DateTimeField('date published',default=datetime.now)
     image = models.ImageField(
          upload_to=get_upload_path, default='place_image.png')
     
     def __str__(self):
        return self.title


class Comment(models.Model):
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        content_list = models.ForeignKey(Product, on_delete=models.CASCADE)
        content = models.TextField()
        create_date = models.DateTimeField(auto_now_add=True)
        modify_date = models.DateTimeField(auto_now=True)

