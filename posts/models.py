from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hashtag(models.Model):
    title = models.CharField(max_length=50)
    posts = models.ManyToManyField('Post', null=True, blank=True)

    def str(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    hashtags = models.ManyToManyField(Hashtag, null=True, blank=True)

    def str(self):
        return f'{self.title}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def str(self):
        return f'{self.author.username}, {self.text}'