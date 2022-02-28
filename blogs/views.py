from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by('-created_time')[:10]
    return render(request, 'blogs/index.html', {'latest_posts': latest_posts})

def detail(request, post_id):
    post = Post.objects.get(pk = post_id)
    post_text = str(post)
    return HttpResponse(f"Post #{post_id}: {post_text}")