from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):

    pass

    avatar = models.ImageField(null=True, blank=True)
    company = models.CharField(max_length=80, default="")
    nickname = models.CharField(max_length=80, default="")

    LOGIN_EMAIL = "email"
    LOGIN_KAKAO = "kakao"
    LOGIN_GOOGLE = "google"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "EMAIL"),
        (LOGIN_KAKAO, "KAKAO"),
        (LOGIN_GOOGLE, "GOOGLE"),
    )

    login_method = models.CharField(
        choices=LOGIN_CHOICES, max_length=10, null=True, blank=True
    )

    email_verified = models.BooleanField(default=False)