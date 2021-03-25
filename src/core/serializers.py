from rest_framework import serializers

from .models import Content, User
from .validators import CustomPasswordValidator

password_validator = CustomPasswordValidator()


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = "__all__"
        read_only_fields = ['author']


class UserSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['is_admin']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}},
        }

    def create(self, validated_data):

        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if not self.validated_data['email']:
            raise serializers.ValidationError(
                {'email': 'Users must have an email address'}
            )

        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'Passwords do not match'}
            )

        if not password_validator.validate(password):
            raise serializers.ValidationError(
                {'password': password_validator.get_help_text()}
            )

        return User.objects.create_user(self.validated_data)
