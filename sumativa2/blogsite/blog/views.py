from django.shortcuts import render, HttpResponse
from .models import post, Category, Hashtag

# Create your views here.
def index(request):
    categories = Category.objects.all()
  
    hashtags = Hashtag.objects.all()
  
    publications = post.objects.all().order_by('-fecha').values()
    context = {
        'publications': publications, 
        'categories': categories,
        'hashtags': hashtags,
 }
    return render(request, 'index.html', context)