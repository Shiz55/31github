from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from account.models import CustomUser

class groups(BaseUserManager):
    def _create_item(self, CustomUser, password, **kwargs):
        if not CustomUser:
            return ValueError('Email должен бфть обязательно передан')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        user.set_password(password)
        user.save()
        return user

class item(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    activation_code = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    is_active = models.BooleanField(default=False,
                                    help_text='Данное полу служит для активации пользователей')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code

    def create_phone_number_code(self):
        code = get_random_string(6, allowed_chars='123456789')
        self.activation_code = code
        return code