from django.http import HttpResponse
from django.shortcuts import render
from article.models import *

# Create your views here.
def home_veiw(request):
    return render(request, 'home.html',{})

def learn_veiw(request):
    categories = LearnCategories.objects.all()
    categoryItems = LearnCategoryItem.objects.all()
    categoryGroups = groupItems(categoryItems)
    

    context = { 'categories':categories, 'categoryItems':categoryItems, "categoryGroups":categoryGroups}
    return render(request, 'learn.html',context)

def practice_veiw(request):
    categories = PracticeCategories.objects.all()
    categoryItems = PracticeCategoryItem.objects.all()
    categoryGroups = groupItems2(categoryItems)

    context = { 'categories':categories, 'categoryItems':categoryItems, "categoryGroups":categoryGroups }
    return render(request, 'practice.html',context)

def about_view(request):
    return render(request, 'base.html', {})




# HELPER FUNCTIONS
def groupItems(categoryItems):
    categoryGroups = []
    group = []
    idx = 0
    for i in range(len(categoryItems)):
        
        if(idx % 3 == 0 and i != 0):
            print("iter: "+str(idx) + " group len: "+ str(len(group)) ) 
            #printList(group)
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

def groupItems2(categoryItems):
    m = {}
    group = []
    for item in categoryItems:
        key = item.category.type;
        if(key in m):
            m[key].append(item);
        else:
            m[key] = [item];
    
    for key in m:
        group.append(m[key]);
    
    return group;


    
def printList(list):
    for item in list:
        print(item.itemName)