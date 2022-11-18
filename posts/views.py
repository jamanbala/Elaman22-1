from django.shortcuts import render
from .models import Hashtag, Post, Comment


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


def comment_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        comments = Comment.objects.filter(post=post)
        data = {
            'post': post,
            'comments': comments
        }
        return render(request, 'posts/post_detail.html', context=data)