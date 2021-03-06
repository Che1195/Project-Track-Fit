# Generated by Django 3.0.5 on 2020-04-12 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_createdworkout_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutexercise',
            name='workout',
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='reps',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='sets',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='WorkoutBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('workout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='workouts.CreatedWorkout')),
            ],
        ),
        migrations.AddField(
            model_name='workoutexercise',
            name='block',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='workouts.WorkoutBlock'),
        ),
    ]
