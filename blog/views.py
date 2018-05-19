from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

from .forms import newBlogPostForm

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

    return render(request, 'base.html', {'form':form})
