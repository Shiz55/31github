from rest_framework import serializers
from rest_framework.authtoken.admin import User



class RegisterPhoneSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    password_configuration = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'last_name', 'first_name')
    pass
