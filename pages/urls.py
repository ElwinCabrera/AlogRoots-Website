from django.urls import path, include
from .views import home_veiw, learn_veiw, practice_veiw

urlpatterns = [
    path('', home_veiw, name="home_view"),
    path('learn/', learn_veiw,name="learn_view"),
    path('practice/', practice_veiw, name="practice_view"),
    path('about/', learn_veiw, name="about_view"),
    path('learn/topic/', include('article.urls')),
    
]