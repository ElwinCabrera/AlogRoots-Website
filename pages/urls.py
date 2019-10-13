from django.urls import path, include
from .views import home_veiw, learn_veiw, learn_topic_veiw

urlpatterns = [
    path('', home_veiw, ),
    path('learn/', learn_veiw),
    path('practice/', learn_veiw),
    path('about/', learn_veiw),
    path('learn/topic/', include('article.urls')),
    
]