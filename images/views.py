from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image


# Create your views here.
def index(request):
    '''
    Index function loads the start up page with a filter of randon six images at the beginning
    '''
    return render(request,'index.html')
   

def gallery(request):

    gallery=Image.objects.all()
    return render(request,'gallery/gallery.html',{'gallery':gallery})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
