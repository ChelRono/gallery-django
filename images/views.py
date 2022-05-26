from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image


# Create your views here.
def index(request):
    '''
    Index function loads the start up page with a filter of randon six images at the beginning
    '''
    return render(request,'gallery/base.html')
    # gallery = Image.objects.all()[:6]
    # return render(request,'index.html', {'gallery':gallery})

def gallery(request):

    gallery=Image.objects.all()
    return render(request,'gallery/gallery.html',{'gallery':gallery})
