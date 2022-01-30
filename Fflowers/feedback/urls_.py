
from django.urls import path, include
from . import views

urlpatterns = [
path('/feedback', views.Feedback_all.as_view(), name='feedback'),
]