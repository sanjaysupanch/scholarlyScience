from rest_framework import serializers
from accounts.models import CustomUser
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    full_name = serializers.CharField(required=True, write_only=True)
    phone_number = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'full_name', 'phone_number', 'password']

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    "A user is already registered with this e-mail address.")
        return email

    def get_cleaned_data(self):
        return {
            'full_name': self.validated_data.get('full_name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'phone_number')
        read_only_fields = ('email', )

