from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'last_login')

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



# users/serializers.py

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs['email']
        if not User.objects.filter(email=email).exists():
            raise ValidationError("There is no user registered with this email address.")
        return super().validate(attrs)


# users/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, force_str
from rest_framework.exceptions import ValidationError

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=100, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationError('The reset link is invalid or has expired.')

            user.set_password(password)
            user.save()

            return user

        except Exception as e:
            raise ValidationError('The reset link is invalid or has expired.')

        return super().validate(attrs)
