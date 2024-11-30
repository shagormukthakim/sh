from django.urls import path
from . import views



urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('', views.dashboard, name='dashboard'),
    path('update/<int:pk>/', views.update_selling_price, name='update_selling_price'),
]

