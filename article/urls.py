from django.urls import path, include
from .views import article_view

urlpatterns = [
    path('<int:article_id>/', article_view, name="article_view" ),
]