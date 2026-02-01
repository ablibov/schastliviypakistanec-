from django.shortcuts import render
from core.models import *

def home(request):
    partners = Partner.objects.all()
    blogs = Blog.objects.order_by("-id")
    features = Feature.objects.order_by("-id")
    context = {
        'partners' : partners,
        'blogs' : blogs, 
        'features' : features,
    }
    return render(request, 'index.html', context)