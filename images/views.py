from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image


# Create your views here.
def index(request):
    '''
    Index function loads the start up page with a filter of randon six images at the beginning
    '''
    gallery = Image.objects.all()[:6]
    return render(request,'index.html', {'gallery':gallery})
