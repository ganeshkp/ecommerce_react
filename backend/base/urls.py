from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.getRoutes, name="routes"),
    path('api/products/', views.getProducts, name='products'),
    path('api/products/<str:pk>/', views.getProduct, name='product')
]