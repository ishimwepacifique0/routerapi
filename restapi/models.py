from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phonenumber = models.IntegerField()
    email = models.CharField(max_length=255)