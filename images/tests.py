from unicodedata import category
from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.

class CategoryTestClass(TestCase):

    def setUp(self):
        self.valarie=Category(name="Travel")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.valarie,Category))

     # Testing Save Method
    def test_save_method(self):
        self.valarie.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)