from django.contrib import admin
from django.urls import path, include
from posts.views import *
from django.conf.urls.static import static
from Blog2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_view),
    path('hashtags/', hashtags_view),
    path('posts/<int:id>/', post_detail_view),
    path('posts/create/', post_create_view),
    path('users/', include('users.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)