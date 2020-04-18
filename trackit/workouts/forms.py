# https://stackoverflow.com/questions/30911612/how-can-i-set-a-datefield-format-in-django-from-the-model
from django import forms
from django.contrib.auth.models import User
from . import models

class CreatedWorkoutForm(forms.ModelForm):

    class Meta():
        model = models.CreatedWorkout
        fields = ['name',]

class WorkoutBlockForm(forms.ModelForm):

    class Meta():
        model = models.WorkoutBlock
        fields = ['name','workout',]
 # https://stackoverflow.com/questions/24041649/filtering-a-model-in-a-createview-with-get-queryset
        # def __init__(self, *args, **kwargs):
        #     user = kwargs.pop('user')
        #     super(WorkoutBlockForm, self).__init__(*args, **kwargs)
        #     self.fields['workout'].queryset = Folder.objects.filter(user=trainer)

class WorkoutExerciseForm(forms.ModelForm):

    class Meta():
        model = models.WorkoutExercise
        fields = ['name','sets','reps','weight','block',]
