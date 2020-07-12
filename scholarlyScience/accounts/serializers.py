from rest_framework import serializers
from accounts.models import CustomUser
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from allauth.utils import (email_address_exists,   get_username_max_length)
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.encoding import force_text
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder


UserModel = CustomUser

class RegisterSerializer(serializers.Serializer):
    username = None
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    full_name = serializers.CharField(required=True, write_only=True)
    phone_number = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(
        max_length=255, style={'input_type': 'password'})

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    "A user is already registered with this e-mail address.")
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def custom_signup(self, request, user):
        user.full_name = self.validated_data.get('full_name', '')
        user.phone_number = self.validated_data.get('phone_number', '')
        user.save(update_fields=['full_name', 'phone_number'])

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'full_name': self.validated_data.get('full_name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'password1': self.validated_data.get('password1', ''),

        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


class LoginSerializer(RestAuthLoginSerializer):
    username = None


# class TokenSerializer(TokenSerializer):
#     """
#     Serializer for Token model.
#     """
#     # pass
#     class Meta:
#         model = TokenModel
#         fields = ('key',)


class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'phone_number')
        read_only_fields = ('email', )


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()

    set_password_form_class = SetPasswordForm

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        self._errors = {}

        # Decode the uidb64 to uid to get User object
        try:
            uid = force_text(uid_decoder(attrs['uid']))
            self.user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError({'uid': ['Invalid value']})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Invalid value']})

        return attrs

    def save(self):
        return self.set_password_form.save()
