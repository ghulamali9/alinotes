from django.db import models
import datetime
from taggit.managers import TaggableManager
from django_summernote.fields import SummernoteTextField


class Auther(models.Model):
    auther_name = models.CharField(max_length=250)
    auther_email = models.EmailField()
    is_updated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(auto_now=False,null=True)
    deleted_at = models.DateField(auto_now=False,null=True)
    def __str__(self):
        return self.auther_name


class Articles(models.Model):
    article_title = models.CharField(max_length=250)
    article_desc = models.CharField(max_length=300)
    article_keywords = models.CharField(max_length=1000)
    article_slug = models.SlugField(max_length=200)
    article_auther = models.ForeignKey(Auther, on_delete = models.CASCADE)
    article_img = models.ImageField(upload_to = 'article_imgs')
    article_date = models.DateField(default=datetime.date.today)
    article_content = SummernoteTextField()
    article_tags = TaggableManager(blank=True)
    is_updated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(auto_now=False,null=True)
    deleted_at = models.DateField(auto_now=False,null=True)
    def __str__(self):
        return self.article_slug


class Comments(models.Model):
    comments_persons_name = models.CharField(max_length=50)
    comments_content = models.TextField()
    comments_persons_email = models.EmailField(max_length=250)
    comments_of_article = models.ForeignKey(Articles, on_delete=models.CASCADE,related_name='comments')
    is_updated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(auto_now=False,null=True)
    deleted_at = models.DateField(auto_now=False,null=True)
    class Meta:
        ordering = ['created_at']


class Messages(models.Model):
    messages_name = models.CharField(max_length=50)
    messages_email = models.EmailField()
    messages_content = models.TextField()
    is_updated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(auto_now=False,null=True)
    deleted_at = models.DateField(auto_now=False,null=True)
