from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Articles,Comments
from django.core.paginator import Paginator
from taggit.models import Tag
from .forms import CommentsForm,ContactMessageForm
from dashboard.mixins import AjaxFormMixin
from django.http import HttpResponse,JsonResponse
from django.core import serializers


#Home Page Section
class Home(View):
    def get(self,request,*args,**kwargs):
        articles = Articles.objects.all().exclude(is_deleted=True).order_by('-id')
        paginator = Paginator(articles, 3)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        common_tags = Tag.objects.all()
        return render(request,'articles/index.html',{'articles' : articles,'common_tags': common_tags})

#Article Page Section
class ArticleDetails(View,AjaxFormMixin):
    def get(self,request,slug,*args,**kwargs):
        get_article = Articles.objects.get(article_slug=slug)
        comments = get_article.comments.all()
        common_tags = Tag.objects.all()
        form = CommentsForm()
        return render(request,'articles/article-details.html',{
        'article' : get_article,
        'common_tags': common_tags,
        'form' : form,
        'comments' : comments
        })

    def post(self,request,slug,*args,**kwargs):
        if request.method == 'POST':
            get_article = Articles.objects.get(article_slug=slug)
            new_comment = None
            form = CommentsForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.comments_of_article = get_article
                new_comment.save()
        return HttpResponse()

#TagsBasedArticlesSearch Page Section
class TagsBasedArticlesSearch(View):
    def get(self,request,slug,*args,**kwargs):
        tag = get_object_or_404(Tag,slug=slug)
        articles = Articles.objects.filter(article_tags=tag)
        paginator = Paginator(articles, 3)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        common_tags = Tag.objects.all()
        return render(request,'articles/tags-search.html',{'articles' : articles,'common_tags': common_tags})


#Contact section
class Contact(View,AjaxFormMixin):
    def get(self,request,*args,**kwargs):
        contact_form = ContactMessageForm()
        return render(request,'articles/contact.html',{'contact_form' : contact_form})


    def post(self,request,*args,**Kwargs):
        if request.method == 'POST':
            form = ContactMessageForm(request.POST)
            if form.is_valid():
                form.save()
        return HttpResponse()


#Comments section
class PostComments(View):
    def get(self,request,slug,*args,**kwargs):
        article = Articles.objects.get(article_slug=slug)
        comments = article.comments.all()
        data = serializers.serialize('json', comments)
        return JsonResponse({"data":data})


#About section
class About(View):
    def get(self,request,*args,**kwargs):
        return render(request,'articles/about.html')
