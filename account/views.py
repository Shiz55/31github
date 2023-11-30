from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authtoken.admin import User
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from category.models import Category

# Create your views here.
User = get_user_model()
class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny, )


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAdminUser)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]


class RegistrationPhoneView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterPhoneSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Успешно зарегистрирован', status=201)


class ActivationPhoneView(APIView):
    pass