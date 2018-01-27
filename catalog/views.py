from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre

# function base


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request,
                  'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors,
                           'num_visits': num_visits})


from django.views import generic
# class base


class BookListView(generic.ListView):
    model = Book
    # the number of items show on one page
    paginate_by = 6


    '''
    # You can add attributes to change the default behaviour above.
    # your own name for the list as a template variable
    context_object_name = 'my_book_list'
    queryset = Book.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war

    # Specify your own template name/location
    template_name = 'books/my_arbitrary_template_name_list.html'
    '''

    # Overriding methods in class-based views    
    '''
    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    '''

    

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 6


class AuthorDetailView(generic.DetailView):
    model = Author
