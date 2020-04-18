from django.db import models
from django.urls import reverse
from django.contrib import auth
from embed_video.fields import EmbedVideoField

# Create your models here.
# class User(auth.models.User, auth.models.PermissionsMixin):
#
#     def __str__(self):
#         return self.usernmae

class Exercise(models.Model):
    CONTRACTION_TYPES = [
        ('Con','Concentric'),
        ('Ecc','Eccentric'),
        ('Iso','Isometric'),
        ('Non','Non-Specific')
    ]
    MOVEMENT_TYPES = [
        ('UPH','Upper Body Push'),
        ('UPL','Upper Body Pull'),
        ('LPH','Lower Body Push'),
        ('LPL','Lower Body Pull'),
        ('COR','Core'),
        ('COM','Combination'),

    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    contraction_type = models.CharField(max_length=3,choices=CONTRACTION_TYPES,
                                        blank=True)
    movement_type = models.CharField(max_length=3,choices=MOVEMENT_TYPES,
                                     blank=True)
    video = EmbedVideoField(blank=True)  # same like models.URLField()

    def __str__(self):
        return self.name.capitalize()

    def get_absolute_url(self):
        return reverse('exercise_database:exercise_list')
