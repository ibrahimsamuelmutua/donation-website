from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='static/img/events/',blank=False, null=False)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    is_admin = models.BooleanField('admin', default=False)

    def __str__(self):
        return self.username
