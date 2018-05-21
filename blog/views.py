from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .forms import newBlogPostForm
from .models import BlogPost


def list_blog_post(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/list.html', {'posts':posts})

def detail_blog_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'blog/detail.html', {'post':post})

def new_blog_post(request):

    if request.method == "POST":
        form = newBlogPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.date = timezone.now()
            model_instance.save()
            return HttpResponse('success')
    else:
        form = newBlogPostForm()

    return render(request, 'blog/new.html', {'form':form})
