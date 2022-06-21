from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model.


# Contact Model
class Contact(models.Model):
    email_address = models.EmailField(max_length=255)
    message = models.TextField(max_length=512)

    def __str__(self):
        return self.email_address