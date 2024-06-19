from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Shop(TemplateView):
    template_name = 'shop.html'

class Cart(TemplateView):
    template_name = 'cart.html'

class Checkout(TemplateView):
    template_name = 'checkout.html'

class Details(TemplateView):
    template_name = 'detail.html'

class Contact(TemplateView):
    template_name = 'contact.html'