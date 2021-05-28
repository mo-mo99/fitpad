from django.test import TestCase, Client
from django.urls import reverse
from .models import *

class TestPosts(TestCase):

    def test_get_show_post(self):
        client = Client()
        response = client.get(reverse('show-post'), kwargs={'pk':2})

        self.assertEqual(response.status_code, 200)
        