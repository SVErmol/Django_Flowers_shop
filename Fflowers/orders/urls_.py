from django.urls import path
from . import views

urlpatterns = [
path('', views.Orders_all_p.as_view(), name='history'),


]