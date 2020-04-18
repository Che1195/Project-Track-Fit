from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class CreatedWorkout(models.Model):
    trainer = models.ForeignKey(User, related_name='trainer_workouts', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workouts:show_workout", kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-date_created']
        # unique_together = ['user','message']

class WorkoutBlock(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    workout = models.ForeignKey(CreatedWorkout,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='blocks',)
    def __str__(self):
        return self.name #+ ', WORKOUT: ' + self.workout.name

    def get_absolute_url(self):
        return reverse("workouts:show_workout", kwargs={'pk':self.workout.pk})

class WorkoutExercise(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    sets = models.PositiveIntegerField(blank=True,null=True)
    reps = models.CharField(max_length=100,blank=True,null=True)
    weight = models.CharField(max_length=100,blank=True,null=True)
    block = models.ForeignKey(WorkoutBlock,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='exercises',)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workouts:show_workout", kwargs={'pk':self.block.workout.pk})
