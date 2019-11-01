from django.shortcuts import render
from .models import *
from django.http import Http404

# Create your views here.

def learn_article_view(request, article_id):
    article = Article.objects.get(pk=article_id)

    if(article.article_type != Choices.LEARN_ARTICLE):
        raise Http404("Article does not belong to the learn section")

    sections = Section.objects.filter(article__id=article_id)
    sub_sections = SubSection.objects.filter(article__id=article_id)
    strengths = Strengths.objects.filter(article__id=article_id)
    weaknesses = Weaknesses.objects.filter(article__id=article_id)
    complexity = Complexity.objects.filter(article__id=article_id)[0];

    resources = ResourcesCitations.objects.filter(article__id=article_id);

    

    context = { "article":article, 
                "sections":sections, 
                "sub_sections":sub_sections,
                "strengths":strengths,
                "weaknesses":weaknesses,
                "complexity":complexity,
                "resources":resources,}

    return render(request, "learn-topic.html", context);

def practice_article_view(request, article_id):
    
    article = Article.objects.get(pk=article_id)
    
    if(article.article_type != Choices.PRACTICE_ARTICLE):
        raise Http404("Article does not belong to the practice section")
    
    sections = Section.objects.filter(article__id=article_id)
    sub_sections = SubSection.objects.filter(article__id=article_id)
    resources = ResourcesCitations.objects.filter(article__id=article_id);

    context = { "article":article, 
                "sections":sections, 
                "sub_sections":sub_sections,
                "resources":resources,}

    return render(request, "practice-topic.html", context);
    

# def group_subsections_to_sections(sections):
#     section_map = {}
    
#     for section in sections:
#         subsections= SubSection.objects.filter(section__id=section.id)
#         section_map[section] = subsections;

#     return section_map