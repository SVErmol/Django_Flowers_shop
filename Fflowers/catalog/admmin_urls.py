from django.urls import path
from . import views

urlpatterns = [

path('products/', views.Products_all.as_view(), name='products'),

path('products/<int:pk>', views.Product_info_ad.as_view(), name='product_info_ad'),
path('products/add', views.Product_add.as_view(), name='product_add'),
path('products/<int:pk>/change', views.Product_change.as_view(), name='change_product'),
path('products/category', views.Category.as_view(), name='category'),
path('products/category/add', views.Category_add.as_view(), name='category_add'),


]