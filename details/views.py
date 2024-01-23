from django.shortcuts import render
from .models import Category, Item

# Create your views here.

def home(request):
    return render(request,'home.html');

def appetizer(request):
    # Assuming 'Appetizer' is the name of the appetizer category
    appetizer_category = Category.objects.get(name='Appetizer')
    appetizers = Item.objects.filter(category=appetizer_category)
    return render(request, 'appetizer.html', {'appetizers': appetizers})

