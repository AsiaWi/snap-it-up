from .models import Profile
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ProfileListTest(APITestCase):
    '''
    Profile creation upon registration test.
    '''
    def setUp(self):
        user = User.objects.create_user(username="TestUser",
                                        password="TestPassword")

    def test_profile_created_on_registration(self):
        response = self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 1)


class ProfileDetailsTest(APITestCase):
    '''
    Profile detail view tests. Retrieve and Update methods for authorised
    and unauthorised users. Delete tested for buyers and sellers safety.
    '''
    def setUp(self):
        user = User.objects.create_user(username="TestUser",
                                        password="TestPassword")
        secondUser = User.objects.create_user(username="SecondTestUser",
                                              password="SecondTestPassword")

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get("/profiles/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_profile_when_authorised(self):
        self.client.login(username='TestUser', password='TestPassword')
        response = self.client.put('/profiles/1/', {
           'location': 'new location'
            })
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.location, 'new location')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_profile(self):
        self.client.login(username='TestUser', password='TestPassword')
        response = self.client.put('/profiles/2/', {
                                                    'location': 'new location'
                                                   })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cant_delete_own_profile_authorised(self):
        self.client.login(username='TestUser', password='TestPassword')
        response = self.client.delete('/profiles/1/')
        self.assertTrue(Profile.objects.filter(pk=1).exists())
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_user_cant_delete_profile_unauthorised(self):
        self.client.login(username='secondTestUser',
                          password='SecondTestPassword')
        response = self.client.delete(f'/profiles/1/')
        self.assertTrue(Profile.objects.filter(pk=1).exists())
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
