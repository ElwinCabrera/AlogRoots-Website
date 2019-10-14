from django.urls import path, include
from .views import home_veiw, learn_veiw, practice_veiw

urlpatterns = [
    path('', home_veiw, ),
    path('learn/', learn_veiw),
    path('practice/', practice_veiw),
    path('about/', learn_veiw),
    path('learn/topic/', include('article.urls')),
    
]