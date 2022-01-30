from django.urls import path
from . import views

urlpatterns = [
path('clients/', views.Clients_all.as_view(), name='clients'),
path('clients/<int:pk>', views.Client_info.as_view(), name='client_info'),
path('clients/add', views.Client_add.as_view(), name='client_add'),
path('clients/<int:pk>/change', views.Client_change.as_view(), name='change_client'),
path('clients/<int:pk>/delete', views.User_delete.as_view(), name='delete_client'),


path('employees/', views.Employees_all.as_view(), name='employees'),
path('employees/<int:pk>', views.Employee_info.as_view(), name='employee_info'),
path('employees/add', views.Employee_add.as_view(), name='employee_add'),
path('employees/<int:pk>/change', views.Employee_change.as_view(), name='change_employee'),
path('employees/<int:pk>/delete', views.User_delete.as_view(), name='delete_employee'),

]