from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()
from workouts.models import CreatedWorkout
# Create your models here.

class Client(models.Model):
    trainer = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse("clientmanager:client_details" , kwargs={'pk':self.pk})

    class Meta:
        ordering = ['last_name']

class LoggedWorkout(models.Model):
    trainer = models.ForeignKey(User, related_name='logged_workouts', on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, related_name='client_logged_workouts', on_delete=models.CASCADE, null=True)
    workout = models.ForeignKey(CreatedWorkout, related_name='logged_instances', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.workout.name

    def get_absolute_url(self):
        return reverse("clientmanager:client_details" , kwargs={'pk':self.client.pk})

    class Meta:
        ordering = ['date']
