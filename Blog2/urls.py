
from django.contrib import admin
from django.urls import path, include
from products.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('date/', now_data),
    path('goodby/', goodby),
    path('', include('posts.urls'))
]
