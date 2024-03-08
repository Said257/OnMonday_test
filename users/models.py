from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_superuser(email, password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(max_length=120)
    phone = models.CharField(max_length=40)
    # необязательные поля
    email = models.EmailField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'мужчина'),
        ('female', 'женщина'),
        ('other', 'другой')
    ], blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    hobby = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

