from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def home_veiw(request):
    return render(request, 'home.html',{})

def learn_veiw(request):
    categories = Learn_Categories.objects.all()
    categoryItems = Learn_Category_Item.objects.all()
    categoryGroups = groupItems(categoryItems)
    

    context = { 'categories':categories, 'categoryItems':categoryItems, "categoryGroups":categoryGroups}
    return render(request, 'learn.html',context)

def practice_veiw(request):
    categories = Practice_Categories.objects.all()
    categoryItems = Practice_Category_Item.objects.all()
    categoryGroups = groupItems(categoryItems)

    context = { 'categories':categories, 'categoryItems':categoryItems, "categoryGroups":categoryGroups }
    return render(request, 'practice.html',context)




# HELPER FUNCTIONS
def groupItems(categoryItems):
    categoryGroups = []
    group = []
    idx = 0
    for i in range(len(categoryItems)):
        
        if(idx % 3 == 0 and i != 0):
            print("iter: "+str(idx) + " group len: "+ str(len(group)) ) 
            printList(group)
            categoryGroups.append(group)
            group = []
        if(i != 0 and categoryItems[i-1].category.type != categoryItems[i].category.type):
            idx +=  3 - len(group)
            if(len(group) != 0):
                categoryGroups.append(group)
            group = []
        group.append(categoryItems[i])
        idx+=1    
        
    if(len(group) != 0):
        categoryGroups.append(group)
    
    return categoryGroups
    
def printList(list):
    for item in list:
        print(item.itemName)