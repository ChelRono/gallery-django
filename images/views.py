from unicodedata import category, name
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category, Image, Location


# Create your views here.
def index(request):
    '''
    Index function loads the start up page with a filter of randon six images at the beginning
    '''
    gallery=Image.objects.all()
    return render(request,'index.html',{"gallery":gallery})
   

def gallery(request):

    gallery=Image.objects.all()
    # news = Article.todays_news()
    # return render(request, 'all-news/today-news.html', {"date": date,"news":news})
    return render(request,'gallery/gallery.html',{"gallery":gallery})

def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term  =  request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message  = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "images":searched_images})
    else:
        message = "You have not searched for any category"
        
        return render(request, 'search.html', {"message":message})

def view_location(request):
    
    location=Image.search_by_location(name)

    return render(request,'location.html', {"location":location})

def view_category(request):
    
    category=Image.search_by_category(name)

    return render(request,'category.html', {"category":category})

    
