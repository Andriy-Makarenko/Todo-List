from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Tag, Task
# from .forms import (
#     CookCreationForm,
#     CookExperienceUpdateForm,
#     DishForm,
#     CookSearchForm,
#     DishSearchForm,
#     DishTypeSearchForm,
# )


def index(request):
    """View function for the home page of the site."""

    num_tag = Tag.objects.count()
    num_task = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tag": num_tag,
        "num_task": num_task,
        "num_visits": num_visits + 1,
    }

    return render(request, "tasks/index.html", context=context)


# class DishTypeListView(LoginRequiredMixin, generic.ListView):
#     model = DishType
#     context_object_name = "dish_type_list"
#     template_name = "restaurant/dish_type_list.html"
#     queryset = DishType.objects.all()