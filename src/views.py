from django.shortcuts import render,HttpResponse
from src.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{ 'bag':posts})


# Create your views here.
