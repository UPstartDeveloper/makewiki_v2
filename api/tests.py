from django.test import TestCase
from rest_framework.test import (
    APIRequestFactory, APITestCase
)
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from wiki.models import Page
from api.serializers import PageSerializer
from api.views import PageList, PageOperationsView


class PageListTests(APITestCase):
    def setUp(self):
        '''Instantiate objects needed to test create and list view.'''
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")
        self.view = PageList.as_view()

    def test_create_page(self):
        '''A user is able to create a new Page if they are signed in.'''
        # make an authenticated request to the view
        create_url = reverse('api:wiki_list_or_create')
        data = {'title': "New Page",
                'author': self.user.id,
                'content': 'This is a test page.'}
        post_request = self.factory.post(create_url, data)
        # test that the Page instaniates
        response = self.view(post_request)
        # response = self.client.post(create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
