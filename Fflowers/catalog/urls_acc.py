from django.urls import path
from . import views

urlpatterns = [


path('basket/', views.Basket.as_view(), name='basket'),
path('favorite/', views.Favorite.as_view(), name='favorite'),


]