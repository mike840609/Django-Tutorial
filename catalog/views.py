from django.shortcuts import render
from .models import Book , BookInstance , Author , Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.count()

    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request ,'index.html', context = {'num_books': num_books , 'num_instances': num_instances , 'num_instances_available':num_instances_available , 'num_authors':num_authors ,'num_visits':num_visits} )
