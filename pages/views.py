from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def home_veiw(request):
    return render(request, 'home.html',{})

def learn_veiw(request):
    categories = Learn_Categories.objects.all()
    categoryItems = Learn_Category_Item.objects.all()

    context = { 'categories':categories, 'categoryItems':categoryItems }
    return render(request, 'learn.html',context)

def practice_veiw(request):
    categories = Practice_Categories.objects.all()
    categoryItems = Practice_Category_Item.objects.all()

    context = { 'categories':categories, 'categoryItems':categoryItems }
    return render(request, 'practice.html',context)

