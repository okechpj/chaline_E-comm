
from django.contrib import admin
from django.urls import path, include
from .views import Shop, Cart, Checkout, Details, Contact

urlpatterns = [
    path('shop/',Shop.as_view(), name='shop'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('details/', Details.as_view(), name='details'),
    path('contact/', Contact.as_view(), name='contact')
]
