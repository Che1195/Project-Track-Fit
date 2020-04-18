from django.db import models
from django.contrib import auth
from django.urls import reverse
# Create your models here.
# auth.models.User is a pre-build django user object
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username
