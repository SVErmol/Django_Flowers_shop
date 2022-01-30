from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
def index(request):
    return render(request, 'admmin/index.html')
def set(request):
    return render(request, 'admmin/setting.html')



