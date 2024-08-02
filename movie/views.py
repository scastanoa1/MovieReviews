from django.shortcuts import render
from django. http import HttpResponse
from .models import Movie

# Create your views here.
def home( request):
    #return HttpResponse(' <h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html', {'name':'Sebastián Castaño'})
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies': movies})

def About(request):
    #return HttpResponse(' <h1>Welcom to About Page</h1>')
    return render(request, 'about.html')