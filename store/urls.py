
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('shop/', views.home, name='shop'),
    path('shop/<slug:slug>', views.product_details, name='product_detail'),
    path('shop/<slug:category_slug>/', views.product_details, name='product_details'),
]
