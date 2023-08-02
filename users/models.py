from django.db import models

def get_upload_path(instance, filename):
    return 'products/{}'.format(filename)

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email
