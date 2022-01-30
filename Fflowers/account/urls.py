from django.urls import path, include
from . import views


urlpatterns = [

path('', include('orders.urls_')),
path('', include('catalog.urls_acc')),
path('setting', views.set, name='setting')


]
