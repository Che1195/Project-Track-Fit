from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models

class UserSignUpForm(UserCreationForm):

    class Meta():
        #these fields are coming from the pre-built UserCreationForm
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

        #This Method is OPTIONAL and is for setting up custom labels for the form.
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Address'

# class ClientModelForm(forms.ModelForm):
#     """
#     Model form for clients.
#     """
#
#     class Meta():
#         model = models.Client
#         fields = ['first_name', 'last_name', 'date_of_birth', 'email']
#         # widgets = {
#         #     'date_of_birth': DateOfBirthWidget(order='MDY'),
#         # }
