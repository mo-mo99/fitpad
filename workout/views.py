from django.shortcuts import render
from myApp.views import *
from .forms import *
from django.db.models import F

def show_exer(request):
    mains = MainWorkout.objects.all()

    return render(request, 'html/workouts.html', context={'mains':mains})


def add_main(request):
    user = request.user.person
    if request.method == 'POST':
        form = AddMainWorkOut(request.POST, request.FILES)
        if form.is_valid():
            muscle = form.cleaned_data['goal_muscle']
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            desc = form.cleaned_data['description']

            new_main_work_out = MainWorkout.objects.create(creator=user, goal_muscle=muscle, name=name,
                                                           image=image, description=desc)

            new_main_work_out.save()
            return show_exer(request)
    else:
        form = AddMainWorkOut()
        return render(request, 'html/addworkout.html', context={'form': form})
