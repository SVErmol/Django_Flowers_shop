from django.shortcuts import render
from .models import Purveyors
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
class Purveyors_all(ListView):
    model=Purveyors
    template_name='purveyors/purveyors.html'
    context_object_name='purveyor'
    queryset=Purveyors().get_purveyors()


class Purveyor_info(DetailView):
    model=Purveyors
    template_name='purveyors/card_purveyor.html'
    context_object_name='purveyor'
    