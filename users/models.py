from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    ROLES = [(USER, "Пользователь"), (ADMIN, "Администратор")]


class User(AbstractUser):
    #нейтрализуем уникальное и обязательное поле модели AbstractUser
    username = None

    phone = models.CharField(max_length=20) #тут можно через PhoneNumberField
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.ROLES, default=UserRoles.USER)
    image = models.ImageField(upload_to='images/', null=True)

    objects = UserManager()



    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN  #

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return self.is_admin

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"