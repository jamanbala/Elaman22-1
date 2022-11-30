from django.shortcuts import render, redirect
from .models import Hashtag, Post, Comment
from .forms import CommentCreateForm, PostCreateForm
from users.utils import get_user_from_request


# Create your views here.
def hashtags_view(request):
    if request.method == 'GET':
        data = {
            'hashtags': Hashtag.objects.all(),
            'user': get_user_from_request(request)
        }
        return render(request, 'posts/hashtags.html', context=data)


def posts_view(request):
    if request.method == 'GET':
        hashtag_id = request.GET.get('hashtag_id')
        if hashtag_id:
            posts = Post.objects.filter(hashtag=Hashtag.objects.get(id=hashtag_id))
        else:
            posts = Post.objects.all()
        data = {
            'posts': posts,
            'user': get_user_from_request(request)
        }
        return render(request, 'posts/posts.html', context=data)


def post_detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        data = {
            'post': post,
            'comments': Comment.objects.filter(post=post),
            'form': CommentCreateForm,
            'user': get_user_from_request(request)
        }
        return render(request, 'posts/post_detail.html', context=data)
    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=1,
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            return redirect(f'/posts/{kwargs["id"]}/')
        else:
            post = Post.objects.get(id=kwargs['id'])
            comments = Comment.objects.filter(post=post)

            data = {
                'post': post,
                'comments': comments,
                'form': form,
                'user': get_user_from_request(request)
            }

            return render(request, 'posts/post_detail.html', context=data)


def post_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm,
            'user': get_user_from_request(request)
        }
        return render(request, 'posts/create.html', context=data)
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)

        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description')
            )
            return redirect('/posts/')
        else:
            data = {
                'form': form,
                'user': get_user_from_request(request)
            }
            return render(request, 'posts/create.html', context=data)
