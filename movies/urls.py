
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('genre/<slug:slug>/',views.genre_details, name='genre_details'),
    path('movie/<slug:slug>/',views.movie_details, name='movie_details'),
    path('search/', views.search, name='search'),
]

