from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Content, User
from .serializers import ContentSerializer, UserSerializer


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'head']

    def get_queryset(self):
        user = self.request.user

        if user.is_admin:
            return User.objects.all()

        return User.objects.filter(email=user.email)


class ContentViewSet(ModelViewSet):

    serializer_class = ContentSerializer
    http_method_names = ['get', 'post', 'head', 'patch']

    def get_queryset(self):
        user = self.request.user

        if user.is_admin:
            return Content.objects.all()

        return Content.objects.filter(author=user)

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user

        serializer = self.get_serializer(data=data)

        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"success": False},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save(author=user)

        return Response(status=status.HTTP_200_OK)
