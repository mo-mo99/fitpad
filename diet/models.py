from django.db import models
from myApp.models import Person


class MainFood(models.Model):
    creator = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=False, null=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    image = models.ImageField()
    note = models.TextField(max_length=1000, blank=True)
    calories = models.FloatField(blank=True)


class DietPlan(models.Model):
    creator = models.ForeignKey(Person, related_name='diet_creator', on_delete=models.SET_NULL, blank=False, null=True)
    client = models.ManyToManyField(Person, related_name='diet_client')
    public = models.BooleanField(default=True)
    description = models.TextField(max_length=1000, blank=True)

    @property
    def meals(self):
        foods = [i for i in Food.objects.all() if i.diet_plan.id == self.id]
        meals_num = max([i.meal for i in foods])
        result = []
        for i in range(meals_num):
            result[i].append([j for j in foods if j.meal == i])
        return result


class Food(models.Model):
    creator = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=False, null=True)
    main_food = models.ForeignKey(MainFood, on_delete=models.CASCADE, blank=False)
    note = models.TextField(max_length=1000, blank=True)
    weight = models.FloatField(blank=True)
    quantity = models.FloatField(blank=True)
    meal = models.FloatField(blank=False, null=False)
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, blank=True, null=True)
