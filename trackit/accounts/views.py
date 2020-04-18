from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,)
from django.views.generic import (CreateView, ListView, DetailView,
                                  TemplateView, UpdateView, DeleteView)
from braces.views import SelectRelatedMixin

from . import forms
from . import models
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserSignUpForm
    # When someone successfully signs up, they will be reversed back to the login page
    # since it is reverse lazy, it does not execute until they hit submit on the signup button
    success_url = reverse_lazy('clientmanager:client_list')
    template_name = 'accounts/signup.html'
#
# class ClientCreateView(LoginRequiredMixin,CreateView):
#     model = models.Client
#     fields = ('first_name', 'last_name', 'date_of_birth', 'email')
#     template_name = 'accounts/create_client.html'
#
#     def form_valid(self,form):
#         self.object = form.save(commit=False)
#         self.object.trainer = self.request.user
#         self.object.save()
#         return super().form_valid(form)
#
# class ClientListView(LoginRequiredMixin,ListView):
#     context_object_name = 'clients'
#     # select_related = ('trainer')
#     model = models.Client
#
#     def get_queryset(self):
#         return models.Client.objects.filter(trainer=self.request.user)
