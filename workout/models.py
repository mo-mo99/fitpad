from django.db import models
from myApp.models import *


class MainWorkout(models.Model):
    creator = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)
    goal_muscle = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField()
    description = models.TextField(max_length=400, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =''
        return url


class Exercise(models.Model):
    creator = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)
    workOut = models.ManyToManyField(MainWorkout, blank=False)
    set = models.FloatField(blank=False)
    repeat = models.FloatField(blank=False)
    note = models.TextField(max_length=1000, blank=True)


class WorkoutPlan(models.Model):
    creator = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    exercise = models.ManyToManyField(Exercise, blank=False)
    public = models.BooleanField(blank=False)

