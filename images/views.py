from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image


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

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
