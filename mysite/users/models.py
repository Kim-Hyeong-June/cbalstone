from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from PIL import Image


class User(AbstractUser):
    USER_CHOICES = [
        ('R', 'Recruiter'),
        ('E', 'Employee'),
        ('C', 'Customer')
    ]

    name = models.CharField(blank=True, max_length=255)
    profile_photo = models.ImageField(blank=True, null=True)
    website1 = models.URLField(blank=True, null = True)
    website2 = models.URLField(blank=True, null = True)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(blank=True, max_length=20)
    user_type = models.CharField(
        blank=True, max_length=1, choices=USER_CHOICES, default="C"
    )
    location = models.CharField(blank=True, max_length=255)

    likes = models.ManyToManyField(
        "self", related_name="user_likes", blank=True, symmetrical=False
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

