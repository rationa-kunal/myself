from django.db import models
from tinymce.models import HTMLField
from datetime import datetime

class BlogPost(models.Model):
    title = models.CharField(max_length=1000)
    intro = HTMLField()
    post = HTMLField()
    img_url = models.URLField(blank=True)
    date = models.DateField(default=datetime.today)
