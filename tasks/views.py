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


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
