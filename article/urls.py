from django.urls import path, include
from .views import learn_article_view, practice_article_view

urlpatterns = [
    path('learn/<int:article_id>/', learn_article_view, name="learn_article_view" ),
    path('practice/<int:article_id>/', practice_article_view, name="practice_article_view" ),
]