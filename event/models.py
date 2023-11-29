from django.db import models


# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=100, blank=False, null=False)
    event_description = models.CharField(max_length=100, blank=False, null=False)
    venue = models.CharField(max_length=100, blank=False, null=False)
    minimum_amount = models.CharField(max_length=100, blank=False, null=False)
    event_date = models.DateField()
    image = models.ImageField(upload_to='static/img/events/')

    def __str__(self):
        return self.event_name
