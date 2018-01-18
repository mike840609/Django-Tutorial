from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # html can call <a href="{% url 'index' %}"> directly . 
    path('',views.index , name = 'index') , 
]
