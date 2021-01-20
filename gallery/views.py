from django.shortcuts import render
from django.views import View
from .models import Gallery as GalleryModel

class Gallery(View):
    def get(self,request,*args,**kwargs):
        gallery = GalleryModel.objects.all()
        context = {
            'gallery' : gallery
        }
        return render(request,'gallery/gallery.html',context)
