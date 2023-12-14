import os
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Advert
from django.contrib.auth.models import User
from rest_framework import status


class AdvertsListTest(APITestCase):
    '''
    Test List View for Advert model
    Setting up a Test User
    Testing Objects can be listed
    Testing if authorised user can create an advert
    Testing if unauthorised user can create advert
    '''
    def setUp(self):
        User.objects.create_user(username='TestUser', password='TestPassword')

    def test_can_list_view_adverts(self):
        TestUser = User.objects.get(username='TestUser')
     
        Advert.objects.create(owner=TestUser, image='default_post', advert_title='TestTitle', price='10.00', item_description='testing')
        response = self.client.get('/adverts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_create_advert_authorised_user(self):
        self.client.login(username='TestUser', password='TestPassword')
        test_image_path = os.path.abspath('snap_it_up/test_image/default_post.jpg')
        # open image file and create SimpleUploadedFile image object
        with open(test_image_path, 'rb') as f:
            test_image = SimpleUploadedFile(os.path.basename(test_image_path), f.read())

        response = self.client.post('/adverts/', {
            'image': test_image,
            'tags': 'test',
            'advert_title': 'TestTitle',
            'price':'10.00',
            'item_description':'testing'
            })
            
        count = Advert.objects.count()
        print(response)
        self.assertEqual(count,1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_advert_unauthorised_user(self):
        test_image_path = os.path.abspath('snap_it_up/test_image/default_post.jpg')

        with open(test_image_path, 'rb') as f:
            test_image = SimpleUploadedFile(os.path.basename(test_image_path), f.read())

        response = self.client.post('/adverts/', {'image': test_image ,'tags': 'test', 'advert_title': 'TestTitle', 'price':'10.00', 'item_description':'testing'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)