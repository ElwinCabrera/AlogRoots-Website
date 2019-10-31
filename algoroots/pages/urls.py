from django.urls import path, include
from .views import home_veiw, learn_veiw, practice_veiw, about_view

urlpatterns = [
    path('', home_veiw, name="home_view"),
    path('learn/', learn_veiw,name="learn_view"),
    path('practice/', practice_veiw, name="practice_view"),
    path('about/', about_view, name="about_view"),
    path('article/', include('article.urls')),
    
]