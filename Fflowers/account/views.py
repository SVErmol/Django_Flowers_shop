from django.shortcuts import render

# Create your views here.
def set(request):
    return render(request, 'account/set.html')