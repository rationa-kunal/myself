from django.urls import path

from . import views as blog_views

urlpatterns = [
    path('new/', blog_views.new_blog_post, name='new_blog_post'),
    path('blog/<int:post_id>/', blog_views.detail_blog_post, name='detail_blog_post'),
    path('', blog_views.list_blog_post, name='list_blog_post'),
]
