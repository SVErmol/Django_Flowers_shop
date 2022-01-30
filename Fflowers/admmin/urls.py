from django.urls import path, include
from . import views

urlpatterns = [
path('', views.index, name='admmin_home'),
path('/setting', views.set, name='set_ad'),
path('', include('users.urls')),
path('', include('orders.urls')),
path('', include('purveyors.urls')),
path('', include('catalog.admmin_urls')),
path('', include('feedback.urls_')),
path('', include('feedback.urls_')),

]