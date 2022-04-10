from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Meal, Ingredient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import MealForm

def toggle_planned(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    if meal.planned:
        meal.planned = False
        meal.save()
        return redirect("home")

    if meal.planned is False:
        meal.planned = True
        meal.save()
        return redirect("home")

# Create your views here.
class MealList(LoginRequiredMixin, generic.ListView):
    model = Meal
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        user_meals = Meal.objects.filter(user=user)
        context = {
            "user_meals": user_meals,
            "meal_form": MealForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        user_meals = Meal.objects.filter(user=user)
        context = {
            "user_meals": user_meals,
            "meal_form": MealForm()
        }

        meal_form = MealForm(data=request.POST)
        if meal_form.is_valid():
            meal_form.instance.user = request.user
            meal = meal_form.save(commit=False)
            meal.save()
            meal_form.save_m2m()
        else:
            meal_form = MealForm()
        return render(request, self.template_name, context)

    
class ShopList(LoginRequiredMixin, generic.ListView):
    model = Meal
    template_name = "list.html"

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        user_meals = Meal.objects.filter(user=user)
        context = {
            'user_meals': user_meals,
        }
        return render(request, self.template_name, context)






