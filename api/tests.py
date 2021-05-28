import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from myApp.models import *
from .serializers import PostSerializer, PersonSerializer


client = Client()


class GetAllPersonsTest(TestCase):

    def test_get_all_persons(self):
        # get API response
        response = client.get(reverse('users-view'))

        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_posts(self):
        response = client.get(reverse('show-post'))

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_get_post(self):
    #     response = client.get(reverse('get-post', kwargs={'pk':4}))
    #     post = Post.objects.get(pk=4)
    #     serializer = PostSerializer(post)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = client.delete(reverse('post-delete', kwargs={'pk':2}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_create_post(self):
        data = {'owner':2, 'text':'heeeey'}
        response = client.post(reverse('post-create'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_post(self):
    #     data = {'owner': 2,'text': 'niceee'}
    #     response = client.put(reverse('post-update', kwargs={'pk':4}), data=json.dumps(data), content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)