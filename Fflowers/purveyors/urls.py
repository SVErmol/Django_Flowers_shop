from django.urls import path
from . import views

urlpatterns = [
path('purveyors/', views.Purveyors_all.as_view(), name='purveyors'),
path('purveyors/<int:pk>', views.Purveyor_info.as_view(), name='purveyor_info'),


]