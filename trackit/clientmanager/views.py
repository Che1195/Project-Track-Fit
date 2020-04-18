from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,)
from django.views.generic import (CreateView, ListView, DetailView,
                                  TemplateView, UpdateView, DeleteView)
from braces.views import SelectRelatedMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from . import models
from . import forms

# Create your views here.
class ClientListView(LoginRequiredMixin,ListView):
    context_object_name = 'clients'
    # select_related = ('trainer')
    model = models.Client

    def get_queryset(self):
        return models.Client.objects.filter(trainer=self.request.user)

class ClientCreateView(LoginRequiredMixin,CreateView):
    model = models.Client
    fields = ('first_name', 'last_name', 'date_of_birth', 'email')
    template_name = 'clientmanager/create_client.html'

    # def get_form(self, *args, **kwargs):
    #     form = super(ClientCreateView, self).get_form(*args, **kwargs)
    #     form.fields['client'].queryset = models.Client.objects.filter(trainer=self.request.user)
    #     return form

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.trainer = self.request.user
        self.object.save()
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Client
    form_class = forms.ClientForm
    template_name = 'clientmanager/client_form_edit.html'

class ClientDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Client
    def get_success_url(self):
        return reverse_lazy('clientmanager:client_list')

class LoggedWorkoutListView(LoginRequiredMixin,ListView):
    context_object_name = 'logged_workouts'
    # select_related = ('trainer')
    model = models.LoggedWorkout

    def get_queryset(self):
        return models.LoggedWorkout.objects.filter(trainer=self.request.user)

class LoggedWorkoutCreateView(LoginRequiredMixin,CreateView):
    model = models.LoggedWorkout
    fields = ('client', 'workout', 'date',)
    template_name = 'clientmanager/create_loggedworkout.html'

    def get_form(self, *args, **kwargs):
        form = super(LoggedWorkoutCreateView, self).get_form(*args, **kwargs)
        form.fields['client'].queryset = models.Client.objects.filter(trainer=self.request.user)
        form.fields['workout'].queryset = models.CreatedWorkout.objects.filter(trainer=self.request.user)
        return form

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.trainer = self.request.user
        self.object.save()
        return super().form_valid(form)


class LoggedWorkoutUpdateView(LoginRequiredMixin,UpdateView):
    model = models.LoggedWorkout
    form_class = forms.LoggedWorkoutForm
    template_name = 'clientmanager/edit_loggedworkout.html'

class LoggedWorkoutDeleteView(LoginRequiredMixin,DeleteView):
    model = models.LoggedWorkout
    def get_success_url(self):
        client_id = self.object.client.pk
        return reverse_lazy('clientmanager:client_details', kwargs={'pk':client_id})

# View for showing the clients information
@login_required
def show_client(request, pk):
    client = models.Client.objects.get(id=pk)
    logged_workouts = client.client_logged_workouts.all()

    if request.user != client.trainer:
        return HttpResponseRedirect(reverse('home'))

    context = {'client': client, 'logged_workouts': logged_workouts}
    return render(request,'clientmanager/client_details.html', context)

@login_required
def show_logged_workout_list(request):
    logged_workouts = models.LoggedWorkout.objects.filter(trainer=request.user)

    # if request.user != logged_workouts.trainer:
    #     return HttpResponseRedirect(reverse('home'))

    context = {'logged_workouts': logged_workouts}
    return render(request,'clientmanager/loggedworkout_list.html', context)
