# Generated by Django 3.2 on 2021-05-15 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_user_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='client',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='workOut',
        ),
        migrations.RemoveField(
            model_name='fitplan',
            name='client',
        ),
        migrations.RemoveField(
            model_name='fitplan',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='fitplan',
            name='diet_plan',
        ),
        migrations.RemoveField(
            model_name='fitplan',
            name='workout_plan',
        ),
        migrations.RemoveField(
            model_name='food',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='food',
            name='diet_plan',
        ),
        migrations.RemoveField(
            model_name='food',
            name='main_food',
        ),
        migrations.RemoveField(
            model_name='like',
            name='liker',
        ),
        migrations.RemoveField(
            model_name='mainfood',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='mainworkout',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='post',
            name='owner',
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
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='DietPlan',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='FitPlan',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='MainFood',
        ),
        migrations.DeleteModel(
            name='MainWorkout',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='WorkoutPlan',
        ),
    ]