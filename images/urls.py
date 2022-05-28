from django.urls import re_path as  url
from . import views



urlpatterns=[

    url(r'^$', views.index, name = 'index'),
    url(r'^gallery/$', views.gallery, name = 'gallery'),
    url(r'^search/', views.search_results, name='search_results')
]
