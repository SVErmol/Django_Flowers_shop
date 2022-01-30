from django.urls import path
from . import views

urlpatterns = [


path('<int:pk>', views.Product_info.as_view(), name='product_info'),

path('', views.Products_.as_view(), name='catalog_home'),


]


