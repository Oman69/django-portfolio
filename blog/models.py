import datetime

from django.db import models


class BlogPost(models.Model):
    date_post = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    post_text = models.TextField(default="default title", max_length=1000)
    subtitle = models.CharField
    img = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title



