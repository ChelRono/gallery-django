

from django.urls import re_path as  url
from . import views


urlpatterns=[
    url('^$',views.index,name='home'),
    url('^gallery/$',views.gallery,name='images')
]