from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class User(AbstractBaseUser):

    username = None
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    objects = UserManager()
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )

    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=False, blank=False, default='other')
    birthdate = models.DateTimeField(null=True, blank=True)

    created_by = models.DateTimeField(null=False, blank=False, auto_now=True, editable=False)
    updated_by = models.DateTimeField(null=False, blank=False, auto_now=True)


    def __str__(self) -> str:
        return f'User: {self.pk}-{self.email}'  
