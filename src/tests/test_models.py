import json
from django.urls.base import reverse
from rest_framework import status

from core.models import User
from .test_setup import TestSetUp


class TestUserModel(TestSetUp):

    def test_user_creation(self):
        data = self.user_data
        data['email'] = "user2@email.com"
        data['phone'] = "8956231248"
        # creating a different user than the one already created by the setUp class
        response = self.client.post(self.user_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        credentials = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.login_url, credentials)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_list_authenticated(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_user_detail_retrieve(self):
        response = self.client.get(reverse("user-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)


class TestContentModel(TestSetUp):

    def test_create_content(self):
        with open(self.document_path, encoding="utf-8", errors="ignore") as file:
            data = self.content_data
            data['document'] = file
            response = self.client.post(self.content_url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_content_list_authenticated(self):
        response = self.client.get(self.content_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_content_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.content_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_content_detail_retrieve(self):
        response = self.client.get(reverse("content-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.content_data['title'])

    def test_content_update_by_owner(self):
        update_field = {"title":"New title"}
        response = self.client.patch(reverse("content-detail", kwargs={'pk': 1}), update_field)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['title'], update_field['title'])

    def test_content_update_by_random_user(self):
        data = self.user_data
        data['email'] = "user2@email.com"
        data['phone'] = "8956231248"
        random_user = User.objects.create_user(data)
        self.client.force_authenticate(user=random_user)

        update_field = {"title":"New title"}
        response = self.client.patch(reverse("content-detail", kwargs={'pk': 1}), update_field)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
