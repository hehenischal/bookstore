from django.shortcuts import render
from .models import Genre,Book,Publication,Author
# Create your views here.
def index(request):
    genres = Genre.objects.all()
    books = Book.objects.all()
    features = books[:3]
    publications = Publication.objects.all()
    authors = Author.objects.all()
    context = {
        'genres': genres,
        'books': books,
        'publications': publications,
        'authors': authors,
        'features': features,
    }
    return render(request, 'index.html',context)