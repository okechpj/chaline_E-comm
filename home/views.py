from django.shortcuts import render
from store.models import Product
from category.models import Category

def home(request):
    # Query all products that are available
    products = Product.objects.all()
    categories = Category.objects.all()

    # Prepare context to pass to template
    context = {
        'products': products,
        'categories': categories
    }
    
    # Render the template with context data
    return render(request, 'templates/index.html', context)
