from django import forms
from .models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('img_title','img_file')
        labels = {
            'Title' : 'img_title',
            'Upload File' : 'img_files'
        }
