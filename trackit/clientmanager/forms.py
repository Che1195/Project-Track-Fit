from django import forms
from . import models

class ClientForm(forms.ModelForm):

    class Meta():
        model = models.Client
        fields = ['first_name', 'last_name', 'date_of_birth', 'email',]

class LoggedWorkoutForm(forms.ModelForm):

    class Meta():
        model = models.LoggedWorkout
        fields = ['client', 'workout', 'date',]
