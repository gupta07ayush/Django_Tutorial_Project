from django.db import models

# Create your models here.

# creating services table in database


class Services(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des = models.TextField()
