from django.urls import path

from . import views as blog_views

urlpatterns = [
    path('new/', blog_views.new_blog_post, name='new_blog_post'),
]
