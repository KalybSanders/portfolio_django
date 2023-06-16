from django.db import models
from unittest.util import _MAX_LENGTH

class Contact(models.Model):
    fullName = models.CharField(max_length=100, default="default")
    phoneNumber = models.CharField(max_length=100, default="default")
    email = models.CharField(max_length=100, default="default")
    message = models.CharField(max_length=10000, default="default")
