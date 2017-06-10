from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'auth_token')
        read_only_fields = ('auth_token',)
        extra_kwargs = {
            'username': {'write_only': True},
            'email': {'write_only': True},
            'password': {'write_only': True},
        }

    def validate(self, data):
        email = data.get('email', None)
        if not email:
            raise ValidationError('email is required field')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email already exists')
        return data

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
