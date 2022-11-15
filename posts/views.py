from django.shortcuts import render
from .models import Hashtag, Post


# Create your views here.
def hashtags_view(request):
    if request.method == 'GET':
        data = {
            'hashtags': Hashtag.objects.all()
        }
        return render(request, 'posts/hashtags.html', context=data)


def posts_view(request):
    if request.method == 'GET':
        data = {
            'posts': Post.objects.all()
        }
        return render(request, 'posts/posts.html', context=data)