from rest_framework import serializers
from rest_framework.authtoken.admin import User
from models import groups, item



class RegisterItemSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    password_configuration = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)

    class Meta:
        model = groups
        fields = ('user', 'id', 'description', 'name_of_item', 'count')
    pass

    class Meta:
        model = item
        fields = ('user', 'id', 'description', 'name_of_item', 'count')
    pass