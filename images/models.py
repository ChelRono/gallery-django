

from django.db import models
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist




# Create your models here.
class Location(models.Model):
     name=models.CharField(max_length=225)

          
     def __str__(self):
        return self.name
    
     def save_location(self):
        self.save()
        
    
     def delete_location(self):
        self.delete()

     class Meta:
        ordering = ['name']

class Category(models.Model):
     name=models.CharField(max_length=225)

     def __str__(self):
        return self.name

     
     def save_category(self):
        self.save()

     def delete_category(self):
          self.delete()

# try:
#     category = Category.objects.get(name = 'Travel')
#     print('Category found')
# except ObjectDoesNotExist:
#     print('Category was not found')
#     class Meta:
#         ordering = ['name']


class Image(models.Model):
    name=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    location = models.ForeignKey(Location,related_name='location', on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_path = models.ImageField(upload_to = 'images/', null=True)

    class Meta:
        ordering = ["pub_date"]
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def save_image(self):
        self.save()
    
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        pass
        

    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images
    
    def search_image(category):
        pass
    
    def filter_by_location(location):
        pass
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

    @classmethod
    def search_by_location(cls,search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

# @classmethod
# def search_by_category(cls, category_name):
#     try:
#       img_by_category = cls.objects.filter(category= category_name).all()
#       return img_by_category
#     except ObjectDoesNotExist:
#       message = "There are no images from that category"
#       return message

# @classmethod
# def search_by_location(cls, location_name):
#     try:
#       img_by_location = cls.objects.filter(location= location_name).all()
#       return img_by_location
#     except ObjectDoesNotExist:
#       message = "There are no images from that location"
#       return message