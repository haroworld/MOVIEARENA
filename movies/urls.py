from django.urls import path
from . import views


urlpatterns=[
    path('', views.mainPage,name="mainPage"),
    path('home/',views.homePage, name="home"),

    path('movie/<str:pk>/',views.singleMovie, name='movie'),

    path('movie_search/', views.movies, name='movie_search'),
    path('search_byName/', views.nameSearch, name="search_byname"),
    path('category/', views.categories, name="category"),

]