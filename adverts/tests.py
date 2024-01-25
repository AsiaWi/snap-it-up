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
    Testing if Objects can be listed
    Testing if authorised user can create an advert
    Testing if unauthorised user can create advert
    '''
    test_image_path = os.path.abspath('snap_it_up/test_image/default_post.jpg')

    def setUp(self):
        User.objects.create_user(username='TestUser', password='TestPassword')
        # open image file and create SimpleUploadedFile image object
        with open(self.test_image_path, 'rb') as f:
            self.test_image = SimpleUploadedFile(os.path.basename(
                                             self.test_image_path), f.read())

    def test_can_list_view_adverts(self):
        TestUser = User.objects.get(username='TestUser')
        Advert.objects.create(owner=TestUser,
                              image='default_post',
                              advert_title='TestTitle',
                              price='10.00',
                              item_description='testing')
        response = self.client.get('/adverts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_create_advert_authorised_user(self):
        self.client.login(username='TestUser', password='TestPassword')
        response = self.client.post('/adverts/', {
            'image': self.test_image,
            'tags': 'test',
            'advert_title': 'TestTitle',
            'price': '10.00',
            'item_description': 'testing',
            'contact_dets': '012345',
            'location': 'location'
            })

        count = Advert.objects.count()
        print(response)
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_advert_unauthorised_user(self):
        response = self.client.post('/adverts/',
                                    {'image': self.test_image,
                                     'tags': 'test',
                                     'advert_title': 'TestTitle',
                                     'price': '10.00',
                                     'item_description': 'testing',
                                     'contact_dets': '012345',
                                     'location': 'location'})
        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)


class AdvertDetailTest(APITestCase):
    '''
    Testing for retrieving, updating and deleting adverts in logged in
    and unauthorised state
    '''
    test_image_path = os.path.abspath('snap_it_up/test_image/default_post.jpg')

    def setUp(self):
        FirstTestUser = User.objects.create_user(username='FirstTestUser',
                                                 password='FirstTestPassword')
        SecondTestUser = User.objects.create_user(username='SecondTestUser',
                                                  password='SecondTestPassword'
                                                  )
        # open image file and create SimpleUploadedFile image object
        with open(self.test_image_path, 'rb') as f:
            self.test_image = SimpleUploadedFile(
                os.path.basename(self.test_image_path), f.read())

        self.advert = Advert.objects.create(owner=FirstTestUser,
                                            image='default_post',
                                            advert_title='TestTitle1',
                                            price='10.00',
                                            item_description='testing',
                                            contact_dets='012345',
                                            location='location')
        Advert.objects.create(owner=SecondTestUser,
                              image='default_post',
                              advert_title='TestTitle2',
                              price='10.00',
                              item_description='testing',
                              contact_dets='012345',
                              location='location')

    def test_can_retrieve_advert_using_valid_id(self):
        response = self.client.get('/adverts/1/')
        self.assertEqual(response.data['advert_title'], 'TestTitle1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_advert_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_advert(self):
        self.client.login(username='FirstTestUser',
                          password='FirstTestPassword')
        response = self.client.put('/adverts/1/', {
            'image': self.test_image,
            'tags': 'test',
            'advert_title': 'TestTitle',
            'price': '10.00',
            'item_description': 'testing',
            'contact_dets': '012345',
            'location': 'location'
            })

        advert = Advert.objects.filter(pk=1).first()
        self.assertEqual(advert.advert_title, 'TestTitle')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_advert(self):
        self.client.login(username='FirstTestUser',
                          password='FirstTestPassword')
        response = self.client.put('/adverts/2/', {'advert_title': 'loser'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_advert_authorised(self):
        self.client.login(username='FirstTestUser',
                          password='FirstTestPassword')
        response = self.client.delete(f'/adverts/{self.advert.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Advert.objects.filter(pk=self.advert.pk).exists())

    def test_user_cannot_delete_advert_unauthorised(self):
        self.client.login(username='secondTestUser',
                          password='SecondTestPassword')
        response = self.client.delete(f'/adverts/{self.advert.pk}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Advert.objects.filter(pk=self.advert.pk).exists())
