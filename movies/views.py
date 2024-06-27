from django.shortcuts import render, get_object_or_404
from .models import Movie,Genre
from django.db.models import Q


# Create your views here.
def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html',{
        'movies': movies
    })

def about(request):
    return render(request, 'movies/about.html')

def movie_details(request,slug):
    movie = get_object_or_404(Movie, slug = slug)
    return render(request, 'movies/movie_details.html',{
        'movie':movie
    })
def genre_details(request, slug):
    genre = get_object_or_404(Genre,slug=slug)
    movies = genre.movies.all()
    return render(request,'movies/genre_details.html',{
        'genre':genre,
        'movies':movies
    })

def search(request):
    query = request.GET.get('query', '')
    movies = Movie.objects.filter(Q(title__icontains=query) | Q(description__icontains= query))
    return render(request, 'movies/search.html', {
        'query':query,
        'movies':movies
    })