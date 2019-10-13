from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_veiw(request):
    return render(request, 'home.html',{})

def learn_veiw(request):
    return render(request, 'learn.html',{})

def learn_topic_veiw(request):
    return render(request, 'learn-topic.html',{})

