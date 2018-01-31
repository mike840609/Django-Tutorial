from django.urls import path,re_path
from . import views


urlpatterns = [
    # html can call <a href="{% url 'index' %}"> directly . 
    path('',views.index , name = 'index') , 

    # a class that inherits from an existing view. 
    # look for templates in /application_name/the_model_name_list.html
    # In this case we use '<int:pk>'  to capture the book id, which must be an integer, and pass it to the view as a parameter named pk (short for primary key).
    path('books/', views.BookListView.as_view() , name = 'books'),
    # path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # generic detail view need the parameter pk 
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

    path('authors/', views.AuthorListView.as_view() , name = 'authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'), #Added for challenge
]
