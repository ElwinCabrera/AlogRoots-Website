from django.urls import path
from landing_pg import views

urlpatterns = [ 
    path('', views.main_landing, name='main_landing')
]
