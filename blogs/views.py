from urllib.request import HTTPPasswordMgrWithPriorAuth
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Post

# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by('-created_time')[:10]
    return render(request, 'blogs/index.html', {'latest_posts': latest_posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'blogs/detail.html', {'post': post})

def vote(request, post_id):
    return HttpResponse("Voted")