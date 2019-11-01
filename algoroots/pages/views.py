from django.http import HttpResponse
from django.shortcuts import render
from article.models import *

# Create your views here.
def home_veiw(request):
    return render(request, 'home.html',{})

def learn_veiw(request):
    articles = Article.objects.filter(article_type=Choices.LEARN_ARTICLE)
    articleGroups = groupItemsLearnView(articles)
    

    context = { 'articles':articles, "articleGroups":articleGroups, "categories":Choices.CATEGORY_CHOICES}
    return render(request, 'learn.html',context)

def practice_veiw(request):
    articles = Article.objects.filter(article_type=Choices.PRACTICE_ARTICLE)
    # articleGroups = groupItemsPracticeView(articles)

    context = { 'articles':articles, "categories":Choices.CATEGORY_CHOICES}
    return render(request, 'practice.html',context)

def about_view(request):
    return render(request, 'base.html', {})




# HELPER FUNCTIONS
def groupItemsLearnView(articles):
    articleGroups = []
    group = []
    idx = 0
    for i in range(len(articles)):
        
        if(idx % 3 == 0 and i != 0):
            print("iter: "+str(idx) + " group len: "+ str(len(group)) ) 
            #printList(group)
            articleGroups.append(group)
            group = []
        if(i != 0 and articles[i-1].category != articles[i].category):
            idx +=  3 - len(group)
            if(len(group) != 0):
                articleGroups.append(group)
            group = []
        group.append(articles[i])
        idx+=1    
        
    if(len(group) != 0):
        articleGroups.append(group)
    
    return articleGroups

def groupItemsPracticeView(articles):
    m = {}
    articleGroups = []
    for article in articles:
        key = article.category;
        if(key in m):
            m[key].append(article);
        else:
            m[key] = [article];
    
    for key in m:
        articleGroups.append(m[key]);
    
    return articleGroups;


    
def printList(list):
    for item in list:
        print(item.itemName)