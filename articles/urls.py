from django.urls import path
from .views import (
    Home,
    ArticleDetails,
    TagsBasedArticlesSearch,
    Contact,
    PostComments,
    About
)

urlpatterns = [
    #Home
    path('',Home.as_view(),name="index"),
    #Article Details
    path('posts/<str:slug>',ArticleDetails.as_view(),name="article-details"),
    #TagsBasedArticlesSearch
    path('tags/<str:slug>',TagsBasedArticlesSearch.as_view(),name="tags-search"),
    #ContactForm
    path('contact/',Contact.as_view(),name="contact"),
    #Comments
    path('comments/<str:slug>',PostComments.as_view(),name="post-comments"),
    #about
    path('about/',About.as_view(),name="about")
]
