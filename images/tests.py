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
        # Creating a new editor and saving it
        self.image1= Location(name = 'Nairobi')
        self.image1.save_location()
        
        self.new_image= Image(name = 'Food',description = 'A variety of foods',location = self.image1)
        self.new_image.save()
