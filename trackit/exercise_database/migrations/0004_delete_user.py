# Generated by Django 3.0.5 on 2020-04-13 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('exercise_database', '0003_auto_20200409_1733'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
