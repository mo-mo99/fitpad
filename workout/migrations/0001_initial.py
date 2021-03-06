# Generated by Django 3.2 on 2021-05-27 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set', models.FloatField()),
                ('repeat', models.FloatField()),
                ('note', models.TextField(blank=True, max_length=1000)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myApp.person')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myApp.person')),
                ('exercise', models.ManyToManyField(to='workout.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='MainWorkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_muscle', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, max_length=400)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myApp.person')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='workOut',
            field=models.ManyToManyField(to='workout.MainWorkout'),
        ),
    ]
