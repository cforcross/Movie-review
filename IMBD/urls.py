from django.urls import path
from .views import (MovieListView, MovieDetailView,
                    MovieCategory, MovieLanguage,
                    MovieSearch, movieYear,MostView)

app_name = 'IMBD'

urlpatterns = [
    path('',MovieListView.as_view(),name='movie_list'),
    path('<slug:slug>',MostView.as_view(),name='most'),
    path('category/<str:category>',MovieCategory.as_view(),name='category'),
    path('language/<str:lang>',MovieLanguage.as_view(),name='language'),
    path('search/',MovieSearch.as_view(),name='search'),
    path('<slug:slug>',MovieDetailView.as_view(),name='movie_detail'),
    path('year/<int:year>',movieYear.as_view(),name='year')
]
