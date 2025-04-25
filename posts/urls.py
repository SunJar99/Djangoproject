from django.contrib import admin
from django.urls import path, include
from posts.views import test_view, html_view, item_list_view, post_list_view, post_detail_view, PostListView, PostDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),

    
    path('', include('posts.urls')),


    path("test/", test_view),
    path("html/", html_view),
    path("posts/", post_list_view, name='post_list'), 
    path("posts/<int:post_id>/", post_detail_view, name='post_detail'),
    path('items/', item_list_view, name='item_list'),


    path("api/posts/", PostListView.as_view(), name='api_post_list'),
    path("api/posts/<int:pk>/", PostDetailView.as_view(), name='api_post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)