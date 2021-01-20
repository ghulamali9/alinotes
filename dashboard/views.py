from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View
from articles.forms import (AutherRegistrationForm,ArticlePostForm)
from gallery.forms import GalleryForm
from .mixins import AjaxFormMixin
from django.http import HttpResponse,JsonResponse
from articles.models import Auther,Articles,Messages
from gallery.models import Gallery
from django.template.loader import render_to_string
import datetime
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


#Dashboard Section (Main)
class DashboardHome(View):
    def get(self,request,*args,**kwargs):
        messages = Messages.objects.all().count()
        articles = Articles.objects.filter(is_deleted=False).count()
        user_model = get_user_model()
        users = user_model.objects.filter(is_active=True).count()
        gallery = Gallery.objects.filter(is_deleted=False).count()
        context = {
            'messages' : messages,
            'articles' : articles,
            'users' : users,
            'gallery' : gallery
        }
        return render(request,'dashboard/main.html',context)


#Auther Section
class AutherRegistration(View,AjaxFormMixin):
    def get(self,request,*args,**kwargs):
        if request.method == 'GET':
            form =  AutherRegistrationForm()
        return render(request,'dashboard/auther-register.html',{'form' : form})


    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            form = AutherRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
        return HttpResponse()


class AutherList(View):
    def get(self,request,*args,**kwargs):
        authers = Auther.objects.all()
        return render(request, 'dashboard/auther-list.html', {'authers':authers})


class AutherUpdate(View):
    def get(self,request,id=0,*args,**kwargs):
        data = {}
        auther = get_object_or_404(Auther,id=id)
        form = AutherRegistrationForm(instance=auther)
        context = {
            'form' : form
        }
        data['html_form'] = render_to_string('dashboard/auther-parts/auther-update.html',context,request=request)
        return JsonResponse(data)


    def post(self,request,id=0,*args,**kwargs):
        data = {}
        auther = get_object_or_404(Auther,id=id)
        if request.method == 'POST':
            form = AutherRegistrationForm(request.POST,instance=auther)
            if form.is_valid:
                form.save()
                date = datetime.datetime.strftime(datetime.date.today(),'%Y-%m-%d')
                Auther.objects.filter(pk=id).update(is_updated=True, updated_at=date)
                data['form_is_valid'] = True
                authers = Auther.objects.all()
                data['data_list'] = render_to_string('dashboard/auther-parts/auther-show.html',{'authers' : authers },request=request)
            else:
                data['form_is_valid'] = False
        return JsonResponse(data)


class AutherDelete(View):
    def get(self,request,id=0,*args,**kwargs):
        data = {}
        auther = get_object_or_404(Auther,id=id)
        context = {
            'auther' : auther
        }
        data['html_form'] = render_to_string('dashboard/auther-parts/auther-delete.html',context,request=request)
        return JsonResponse(data)


    def post(self,request,id=0,*args,**kwargs):
        data = {}
        if request.method == 'POST':
            date = datetime.datetime.strftime(datetime.date.today(),'%Y-%m-%d')
            Auther.objects.filter(pk=id).update(is_deleted=True, deleted_at=date)
            data['form_is_valid'] = True
            authers = Auther.objects.all()
            data['data_list'] = render_to_string('dashboard/auther-parts/auther-show.html',{'authers' : authers },request=request)
        return JsonResponse(data)


#Articles Section
from django.contrib import messages
class ArticlePublish(View,AjaxFormMixin):
    def get(self,request,*args,**kwargs):
        if request.method == 'GET':
            form =  ArticlePostForm()
        return render(request,'dashboard/article-publish.html',{'form' : form})


    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            form = ArticlePostForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
        return HttpResponse()


class ArticleList(View):
    def get(self,request,*args,**kwargs):
        articles = Articles.objects.all()
        return render(request,'dashboard/article-list.html',{'articles' : articles})


class ArticleUpdate(View):
    def get(self,request,id=0,*args,**kwargs):
        data = {}
        article = get_object_or_404(Articles,id=id)
        form = ArticlePostForm(instance=article)
        context = {
            'form' : form
        }
        data['html_form'] = render_to_string('dashboard/article-parts/article-update.html',context,request=request)
        return JsonResponse(data)


    def post(self,request,id=0,*args,**kwargs):
        data = {}
        article = get_object_or_404(Articles,id=id)
        if request.method == 'POST':
            form = ArticlePostForm(request.POST,request.FILES,instance=article)
            if form.is_valid:
                form.save()
                date = datetime.datetime.strftime(datetime.date.today(),'%Y-%m-%d')
                Articles.objects.filter(pk=id).update(is_updated=True, updated_at=date)
                data['form_is_valid'] = True
                articles = Articles.objects.all()
                data['data_list'] = render_to_string('dashboard/article-parts/article-show.html',{'articles' : articles },request=request)
            else:
                data['form_is_valid'] = False
        return JsonResponse(data)


class ArticleDelete(View):
    def get(self,request,id=0,*args,**kwargs):
        data = {}
        article = get_object_or_404(Articles,id=id)
        context = {
            'article' : article
        }
        data['html_form'] = render_to_string('dashboard/article-parts/article-delete.html',context,request=request)
        return JsonResponse(data)
    def post(self,request,id=0,*args,**kwargs):
        data = {}
        if request.method == 'POST':
            date = datetime.datetime.strftime(datetime.date.today(),'%Y-%m-%d')
            Articles.objects.filter(pk=id).update(is_deleted=True, deleted_at=date)
            data['form_is_valid'] = True
            articles = Articles.objects.all()
            data['data_list'] = render_to_string('dashboard/article-parts/article-show.html',{'articles' : articles },request=request)
        return JsonResponse(data)


#Dashboard Users Section
class UserRegistration(View,AjaxFormMixin):
    def get(self,request,*args,**kwargs):
        form = UserRegistrationForm()
        context = {
            'form' : form
        }
        return render(request,'dashboard/user-register.html',context)


    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
        return HttpResponse()


#Dashboard Login System
class UserLogin(View):
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request,username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('dashboard-home')
        return render(request,'dashboard/login-page.html',{'form':form})


    def get(self,request,*args,**kwargs):
        form = UserLoginForm()
        return render(request,'dashboard/login-page.html',{'form':form})


#Dashboard Logout System
class UserLogout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('user-login')


#Messages Section
class MessagesReview(View):
    def get(self,request,*args,**kwargs):
        messages = Messages.objects.all()
        return render(request,'dashboard/messages-review.html',{'messages' : messages})


#Gallery section
class GalleryManagement(View,AjaxFormMixin):
    def get(self,request,*args,**kwargs):
        form = GalleryForm()
        gallery = Gallery.objects.all().order_by('created_at')
        return render(request,'dashboard/gallery-management.html',{'form' : form, 'gallery' : gallery})


    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            form = GalleryForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
        return HttpResponse()


class GalleryUpdate(View):
    def get(self,request,id=0,*args,**kwargs):
        data = {}
        gallery = get_object_or_404(Gallery,id=id)
        form = GalleryForm(instance=gallery)
        context = {
            'form' : form
        }
        data['html_form'] = render_to_string('dashboard/gallery-parts/gallery-update.html',context,request=request)
        return JsonResponse(data)


    def post(self,request,id=0,*args,**kwargs):
        data = {}
        gallery = get_object_or_404(Gallery,id=id)
        if request.method == 'POST':
            form = GalleryForm(request.POST or None,request.FILES or None,instance=gallery)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.save()
                date = datetime.datetime.strftime(datetime.date.today(),'%Y-%m-%d')
                Gallery.objects.filter(pk=id).update(is_updated=True, updated_at=date)
                data['form_is_valid'] = True
            else:
                data['form_is_valid'] = False
        return JsonResponse(data)


class GalleryDelete(View):
    def get(self,request,id=0,*args,**kwargs):
        data = {}
        gallery = get_object_or_404(Gallery,id=id)
        context = {
            'gallery' : gallery
        }
        data['html_form'] = render_to_string('dashboard/gallery-parts/gallery-delete.html',context,request=request)
        return JsonResponse(data)

    def post(self,request,id=0,*args,**kwargs):
        data = {}
        if request.method == 'POST':
            date = datetime.datetime.strftime(datetime.date.today(),'%Y-%m-%d')
            Gallery.objects.filter(pk=id).update(is_deleted=True, deleted_at=date)
            data['form_is_valid'] = True
        return JsonResponse(data)
