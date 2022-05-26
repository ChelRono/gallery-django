

from django.urls import re_path as  url
from . import views
import images

urlpatterns=[
    url('^$',views.index,name='welcome'),
    url('^gallery/$',views.gallery,name='images')
]