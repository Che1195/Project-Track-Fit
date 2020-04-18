from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CreatedWorkout)
admin.site.register(models.WorkoutBlock)
admin.site.register(models.WorkoutExercise)
