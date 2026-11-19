from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic

def index (request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_classic_genres = Genre.objects.filter(name__icontains='Классика').count()
    num_fountainhead_books = Book.objects.filter(title__icontains='Источник').count()

    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1

    return render(request, 'index.html', context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_authors': num_authors, 'num_classic_genres': num_classic_genres, 'num_fountainhead_books': num_fountainhead_books, 'num_visits':num_visits})

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'