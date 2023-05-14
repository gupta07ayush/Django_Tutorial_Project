from django.db import models

# Create your models here.


# creating services table in database
class Block(models.Model):
    block_icon = models.CharField(max_length=50)
    block_title = models.CharField(max_length=50)
    block_des = models.TextField()
