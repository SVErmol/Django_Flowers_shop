from django.shortcuts import render
from .models import Feedback
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.





class Feedback_all(ListView):
    model=Feedback
    template_name='feedback/feedback.html'
    context_object_name='feedback'
    # queryset=Users().get_clients()

# Create your views here.
