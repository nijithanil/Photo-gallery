from django.db import models


# Create your models here.

class shop(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to="images")
    location = models.TextField()
    price = models.IntegerField()


class item(models.Model):
    name = models.CharField(max_length=25)
    rate = models.IntegerField()
