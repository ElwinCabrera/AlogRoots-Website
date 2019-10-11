from django.urls import path, include
from .views import home_veiw, learn_categories_veiw, learn_veiw

urlpatterns = [
    path('', home_veiw, ),
    path('learn-categories', learn_categories_veiw),
    path('learn', learn_veiw),
]