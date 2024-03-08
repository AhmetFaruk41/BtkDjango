from turtle import path
from django.http import HttpResponse
from.import views



urlpatterns = [
    path('', views.home),
    path('anasayfa',views.home),
    path('kurslar',views.kurslar),
]
