from django.shortcuts import render
from .models import Reviews

# Create your views here.
def reviews_home(request):
    reviews=Reviews.objects.all()
    return render(request,'reviews/reviews.html',{'reviews':reviews})