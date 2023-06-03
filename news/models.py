from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    date_posted = models.DateTimeField(auto_now_add=True)
    news_title = models.CharField(max_length=255)
    news_content = models.TextField()
    date_updated = models.DateTimeField(auto_now=True)
    is_Published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=1)

    # author_id=

    def __str__(self):
        return self.news_title


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_content = models.TextField()
