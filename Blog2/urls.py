
from django.contrib import admin
from django.urls import path, include
from products.views import *
from django.conf.urls.static import static
from Blog2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('date/', now_data),
    path('goodby/', goodby),
    path('', include('posts.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)