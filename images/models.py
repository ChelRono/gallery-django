from unicodedata import category
from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
     name=models.CharField(max_length=225)

class Category(models.Model):
     name=models.CharField(max_length=225)

class Image(models.Model):
    name=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    # photo = models.ImageField(upload_to = '/')