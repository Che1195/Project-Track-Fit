from django.shortcuts import render
from django.views.generic import (CreateView, ListView, DetailView,
                                  TemplateView,)
from . import models

# Create your views here.
class ExerciseListView(ListView):
    context_object_name = 'exercises'
    model = models.Exercise

    def get_queryset(self):
        return models.Exercise.objects.order_by('name')

class ExerciseCreateView(CreateView):
    model = models.Exercise
    fields = ('name','description','contraction_type','movement_type','video')

class ExerciseDetailView(DetailView):
    model = models.Exercise

class IndexView(TemplateView):
    template_name = 'trackit/index.html'
