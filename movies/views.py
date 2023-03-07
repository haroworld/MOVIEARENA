from unicodedata import category
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import movie,Categories
from django.db.models import Q

# Create your views here.

def mainPage(request):

    if request.method == 'POST':
        request.session['mail'] = request.POST['email']
        return redirect('register')

    
    return render(request, 'movies/index.html')

@login_required(login_url='login')
def homePage(request):
    movies = movie.objects.all
    tvshows = movie.objects.filter(category__movie_category__icontains = 'shows')
    movie_video = movie.objects.filter(category__movie_category__icontains = 'movie')
    cartoons = movie.objects.filter(category__movie_category__icontains = 'cartoon')
    context = {'movies':movies,'tvshows':tvshows,'movie':movie_video,'cartoons':cartoons}
    return render(request, 'movies/home.html', context)


@login_required(login_url='login')
def singleMovie(request,pk):

    single_movie = movie.objects.get(id=pk)
    main_category = single_movie.main_category
    similar_movie = movie.objects.filter(category = main_category).exclude(id = single_movie.id)
    movie_category = single_movie.category.all()
    context = {'movie':single_movie,'movie_category':movie_category,'similar_movie':similar_movie}
    return render(request, 'movies/movie.html', context)

@login_required(login_url='login')
def movies(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    movies = movie.objects.filter(
        Q(category__movie_category__icontains = search_query)
    )

    


    context = {'movies':movies}
    return render(request, 'movies/movie_search.html', context)

@login_required(login_url='login')
def nameSearch(request):
    search_by_name = ''

    if request.GET.get('search_by_name'):
        search_by_name = request.GET.get('search_by_name')
    movies = movie.objects.filter(
        Q(movie_name__icontains = search_by_name)
    )

    


    context = {'movies':movies}
    return render(request, 'movies/search_byname.html', context)

@login_required(login_url='login')
def categories(request):
    category = Categories.objects.all()

    context = {'category':category}
    return render(request, 'movies/categories.html', context)
