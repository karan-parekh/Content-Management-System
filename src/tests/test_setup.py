from django.core.files import File
from rest_framework.test import APITestCase

from core.models import User, Content
from rest_framework.authtoken.models import Token


class TestSetUp(APITestCase):

    def setUp(self):
        self.user_url = "/api/user/"
        self.content_url = "/api/content/"
        self.login_url = "/login/"

        self.user_data =  {
            "full_name": "User",
            "email": "user@email.com",
            "phone": "8956231245",
            "address": "Lorem ipsum",
            "city": "New Jersey",
            "state": "New York",
            "country": "USA",
            "pincode": "445511",
            "password": "Password",
            "confirm_password": "Password",
            "is_admin": False
        }

        self.admin_data = {
            "full_name": "Admin",
            "email": "admin@email.com",
            "phone": "8956531245",
            "address": "Lorem ipsum",
            "city": "New Jersey",
            "state": "New York",
            "country": "USA",
            "pincode": "445511",
            "password": "Password",
            "confirm_password": "Password",
            "is_admin": True
        }

        self.user  = User.objects.create_user(self.user_data)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        self.document_path = "src/tests/data/Karan_Parekh_CV.pdf"

        self.content_data = {
            "author": self.user,
            "title": "Lorem Ipsum",
            "body": "Lorem Ipsum",
            "summary": "Lorem Ipsum",
            "categories": "BOND",
        }
        self.content = self.create_content()

        return super().setUp()

    def create_content(self):
        with open(self.document_path, encoding="utf-8", errors="ignore") as file:
            file = File(file)
            data = self.content_data
            data['document'] = file
            content = Content(**data)
            content.save()
            return content

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def tearDown(self):
        return super().tearDown()