from django.test import TestCase
from .models import Author
# Create your tests here.
class AuthorTestCase(TestCase):
    def setUp(self):
        self.author=Author.objects.create(name="Random Smith")
        
    def test_is_correct_instance(self):
        self.assertIsInstance(self.author,Author)
    
    def test_existe(self):
        author =Author.objects.get(pk=1)
        self.assertFalse(author)