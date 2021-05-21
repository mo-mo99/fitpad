from django.urls import path
from .views import *

urlpatterns = [
    path('', show_exer, name="show_exer"),
    path('addworkout/', add_main, name="add_main_work"),
    path('workouts/', show_exer, name="workouts")
]