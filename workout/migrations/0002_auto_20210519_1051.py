# Generated by Django 3.2 on 2021-05-19 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainworkout',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='workoutplan',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='workoutplan',
            name='exercise',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='MainWorkout',
        ),
        migrations.DeleteModel(
            name='WorkoutPlan',
        ),
    ]
