from django.test import SimpleTestCase
from django.urls import reverse, resolve
from katalog.views import katalog

class TestUrls(SimpleTestCase):
    def test_katalog(self):
        url = reverse('katalog')
        self.assertEquals(resolve(url).func, katalog)