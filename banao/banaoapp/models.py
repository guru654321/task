from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    PROFILE_PICTURE_UPLOAD_TO = 'profile_pictures/'

    profile_picture = models.ImageField(upload_to=PROFILE_PICTURE_UPLOAD_TO, null=True, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    USER_TYPE_CHOICES = (
        ('1', 'Doctor'),
        ('2', 'Patient'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
