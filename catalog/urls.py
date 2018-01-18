from django.urls import path
from . import views


urlpatterns = [
    # html can call <a href="{% url 'index' %}"> directly . 
    path('',views.index , name = 'index') , 
    path('book/', views.BookListView.as_view() , name = 'books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]
