from django.shortcuts import render
from .models import *

# Create your views here.

def learn_article_view(request, article_id):
    article = Article.objects.get(pk=article_id)
    sections = Section.objects.filter(article__id=article_id)
    sub_sections = SubSection.objects.filter(article__id=article_id)
    strengths = Strengths.objects.filter(article__id=article_id)
    weaknesses = Weaknesses.objects.filter(article__id=article_id)
    complexity = Complexity.objects.filter(article__id=article_id)[0];

    context = { "article":article, 
                "sections":sections, 
                "sub_sections":sub_sections,
                "strengths":strengths,
                "weaknesses":weaknesses,
                "complexity":complexity,}

    return render(request, "learn-topic.html", context);

def practice_article_view(request, article_id):
    article = Article.objects.get(pk=article_id)
    sections = Section.objects.filter(article__id=article_id)
    sub_sections = SubSection.objects.filter(article__id=article_id)

    context = { "article":article, 
                "sections":sections, 
                "sub_sections":sub_sections,}

    return render(request, "practice-topic.html", context);
    