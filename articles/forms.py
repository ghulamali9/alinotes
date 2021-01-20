from django_summernote.widgets import SummernoteInplaceWidget
from django import forms
from .models import (
    Articles,
    Auther,
    Comments,
    Messages
    )
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field,Submit,Row,Column


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Articles
        widget = {
            'article_content' : SummernoteInplaceWidget()
        }
        fields = ('article_auther','article_title','article_keywords','article_tags',
        'article_slug','article_img','article_desc','article_content')
        labels = {
        'article_auther' : 'Auther',
        'article_title' : 'Title',
        'article_keywords' : 'Meta Keywords',
        'article_tags' : 'Tags',
        'article_slug' : 'Slug',
        'article_img' : 'Image',
        'article_desc' : 'Meta Description',
        'article_content' : 'Content'
        }


    def __init__(self,*args,**kwargs):
        super(ArticlePostForm,self).__init__(*args,**kwargs)
        self.fields['article_auther'].empty_label = "Select Auther"


class AutherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Auther
        fields = ('auther_name','auther_email')
        labels = {
        'auther_name' : 'Name',
        'auther_email' : 'Email'
        }


    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            val = validate_email(email)
        except:
            raise ValidationError("Invalid Email")
        if Auther.objects.filter(email=email).exists():
            raise ValidationError("Email Already Exists")
        return email


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments_persons_name','comments_persons_email','comments_content')
        labels = {
        'comments_persons_name' : 'Fullname',
        'comments_persons_email' : 'Email',
        'comments_content' : 'Comment'
        }


    def __init__(self,*args,**kwargs):
        super(CommentsForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('comments_persons_name', css_class='form-control rounded-0'),
            Field('comments_persons_email', css_class='form-control rounded-0'),
            Field('comments_content', css_class='form-control rounded-0'),
            Submit('submit', 'Comment', css_class='btn pb_outline-dark pb_font-13 pb_letter-spacing-2  rounded-0 p-3')
        )


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('messages_name','messages_email','messages_content')
        labels = {
        'messages_name' : 'Name',
        'messages_email' : 'Email',
        'messages_content' : 'Message'
        }


    def __init__(self,*args,**kwargs):
        super(ContactMessageForm, self).__init__(*args,**kwargs)
        #self.fields['messages_content'].widget.attrs.update(style='border-radius: 0')
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column(Field('messages_name', css_class='form-control rounded-0'), css_class='col-md-6'),
                Column(Field('messages_email', css_class='form-control rounded-0'), css_class='col-md-6'),
                css_class='form-row'
            ),

            Field('messages_content', css_class='form-control rounded-0'),
            Submit('submit', 'Send Message', css_class='btn pb_outline-dark pb_font-13 pb_letter-spacing-2  p-3 rounded-0')
        )
