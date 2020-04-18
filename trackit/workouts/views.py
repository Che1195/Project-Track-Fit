from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,)
from braces.views import SelectRelatedMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView, ListView, DetailView,
                                  TemplateView, UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from . import forms
from django.contrib import messages
from django.http import Http404

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
#
class CreatedWorkoutListView(LoginRequiredMixin,ListView,SelectRelatedMixin):
    context_object_name = 'workouts'
    select_related = ('trainer')
    model = models.CreatedWorkout

    def get_queryset(self):
        return models.CreatedWorkout.objects.filter(trainer=self.request.user)

class WorkoutCreateView(LoginRequiredMixin,CreateView):
    model = models.CreatedWorkout
    fields = ('name',)
    template_name = 'workouts/workout_form.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.trainer = self.request.user
        self.object.save()
        return super().form_valid(form)

class WorkoutExerciseCreateView(LoginRequiredMixin,CreateView):
    model = models.WorkoutExercise
    fields = ('name','sets','reps','weight','block')
    template_name = 'workouts/workout_exercise_form.html'

class WorkoutBlockCreateView(LoginRequiredMixin,CreateView):
    model = models.WorkoutBlock
    fields = ('name','workout')
    template_name = 'workouts/workout_block_form.html'

# https://stackoverflow.com/questions/47375759/django-createview-display-only-particular-objects-in-foreignkey-field
    def get_form(self, *args, **kwargs):
        form = super(WorkoutBlockCreateView, self).get_form(*args, **kwargs)
        form.fields['workout'].queryset = models.CreatedWorkout.objects.filter(trainer=self.request.user)
        return form

    # def get_queryset(self):
    #     return models.CreatedWorkout.objects.filter(trainer=self.request.user)

    # def form_valid(self,form):
    #     self.object = form.save(commit=False)
    #     self.object.workout = self.request.workout
    #     self.object.save()
    #     return super().form_valid(form)

class WorkoutBlockUpdateView(LoginRequiredMixin,UpdateView):
    model = models.WorkoutBlock
    form_class = forms.WorkoutBlockForm
    template_name = 'workouts/workout_block_form.html'

class WorkoutBlockDeleteView(LoginRequiredMixin,DeleteView):
    model = models.WorkoutBlock

    def get_success_url(self):
        workout = self.object.workout
        return reverse_lazy('workouts:show_workout', kwargs={'pk': workout.pk})

class WorkoutExerciseUpdateView(LoginRequiredMixin,UpdateView):
    model = models.WorkoutExercise
    form_class = forms.WorkoutExerciseForm
    template_name = 'workouts/workout_exercise_form.html'

class WorkoutExerciseDeleteView(LoginRequiredMixin,DeleteView):
    model = models.WorkoutExercise
    def get_success_url(self):
        workout = self.object.block.workout
        return reverse_lazy('workouts:show_workout', kwargs={'pk': workout.pk})

class CreatedWorkoutUpdateView(LoginRequiredMixin,UpdateView):
    model = models.CreatedWorkout
    form_class = forms.CreatedWorkoutForm
    template_name = 'workouts/workout_form_edit.html'

class CreatedWorkoutDeleteView(LoginRequiredMixin,DeleteView):
    model = models.CreatedWorkout
    def get_success_url(self):
        return reverse_lazy('clientmanager:client_list')

def handler404(request, exception):
    return render(request, 'trackit/404.html', status=404)

@login_required
def show_workout(request, pk):
    workout = models.CreatedWorkout.objects.get(id=pk)
    if request.user != workout.trainer:
        return HttpResponseRedirect(reverse('home'))
    blocks = workout.blocks.all()
    block_name_list = []
    block_list = []
    for block in blocks:
        block_name_list.append(block.name)
        exercises = block.exercises.all()
        exercises_list = []
        for exercise in exercises:
            exercises_list.append(exercise)
        block_list.append(exercises_list)

    context = {'workout':workout,
               'blocks':blocks,
               'block_names':block_name_list}
    return render(request,'workouts/show_workout.html',context)

# def create_workout(request):
#     if request.method == 'POST':
#         workout_form = forms.WorkoutForm(data=request.POST)
#
#         if workout_form.is_valid():
#             workout = workout_form.save()
#             user.save()
#
#             created = True
#
#         else:
#             print(workout_form.errors)
#     else:
#         workout_form = forms.WorkoutForm()
#
#     context = {'workout_form':workout_form}
#
#     return render(request,'workouts/function_workout_form.html',context)
