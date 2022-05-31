from unicodedata import category
from django.urls import re_path as  url
from . import views




urlpatterns=[

    url(r'^$', views.index, name = 'index'),
    url(r'^gallery/$', views.gallery, name = 'gallery'),
   url(r'^search/', views.search_category, name = 'search_category'),
    url(r'^location/$', views.view_location, name = 'location'),
    url(r'^category/$', views.view_category, name = 'category')
]