
from unicodedata import category
from django.test import TestCase
from .models import Location,Category,Image


# Create your tests here.

class CategoryTestClass(TestCase):

    def setUp(self):
        self.cat1=Category(name="Travel")
  

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.loc1= Location(name = 'Nairobi')

class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new loaction and saving it
        self.loc1= Location(name = 'Nairobi')
        self.loc1.save_location()

        self.new_cat1=Category(name="Travel")
        self.new_cat1.save_category()
        
        self.new_image= Image(name = 'Food',description = 'A variety of foods',location = self.loc1) 
        self.new_image.save()

        self.new_image.category.add(self.new_cat1)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    
