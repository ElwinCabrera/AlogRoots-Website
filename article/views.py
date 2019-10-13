from django.shortcuts import render
from .models import *

# Create your views here.

def article_view(request, article_id):
    article = Article.objects.get(pk=article_id)
    sections = Section.objects.filter(article__id=article_id)
    sub_sections = SubSection.objects.filter(article__id=article_id)
    goodFor = GoodFor.objects.filter(article__id=article_id)
    notGoodFor = NotGoodFor.objects.filter(article__id=article_id)

    context = { "article":article, 
                "sections":sections, 
                "sub_sections":sub_sections,
                "goodFor":goodFor,
                "notGoodFor":notGoodFor,}

    return render(request, "learn-topic.html", context);
    