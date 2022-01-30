from django.urls import path
from . import views

urlpatterns = [
path('orders/', views.Orders_all.as_view(), name='orders'),
path('orders/<int:pk>', views.Order_info.as_view(), name='order_info'),
path('orders/add', views.Order_add.as_view(), name='order_add'),
path('orders/needed', views.Needed.as_view(), name='needed'),
path('orders/<int:pk>/change', views.Order_change.as_view(), name='change_order'),
# path('orders/<int:pk>/delete', views.Order_delete.as_view(), name='delete_order'),

]