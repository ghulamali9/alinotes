from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import (
    DashboardHome,
    AutherRegistration,
    AutherList,
    AutherUpdate,
    AutherDelete,
    ArticlePublish,
    ArticleList,
    ArticleUpdate,
    ArticleDelete,
    UserRegistration,
    UserLogin,
    UserLogout,
    MessagesReview,
    GalleryManagement,
    GalleryUpdate,
    GalleryDelete
)


urlpatterns = [
    path('',login_required(DashboardHome.as_view(),login_url='user-login'),name="dashboard-home"),
    #Auther Section
    path('register-auther',login_required(AutherRegistration.as_view(),login_url='user-login'),name="auther-registration"),
    path('list-auther',login_required(AutherList.as_view(),login_url='user-login'),name="auther-list"),
    path('edit-auther/<int:id>',AutherUpdate.as_view(),name="auther-edit"),
    path('delete-auther/<int:id>',AutherDelete.as_view(),name="auther-delete"),
    #Article Section
    path('publish-article',login_required(ArticlePublish.as_view(),login_url='user-login'),name="article-publish"),
    path('list-article',login_required(ArticleList.as_view(),login_url='user-login'),name="article-list"),
    path('edit-article/<int:id>',ArticleUpdate.as_view(),name="article-edit"),
    path('delete-article/<int:id>',ArticleDelete.as_view(),name="article-delete"),
    #Dashboard Users Section
    path('register-user',login_required(UserRegistration.as_view(),login_url='user-login'),name="user-registration"),
    #Dashboard Login System
    path('login-user',UserLogin.as_view(),name="user-login"),
    path('logout-user',UserLogout.as_view(),name="user-logout"),
    #Messages Section
    path('messages-review',login_required(MessagesReview.as_view()),name="messages-review"),
    #Gallery section
    path('gallery-management',login_required(GalleryManagement.as_view()),name="gallery-management"),
    path('edit-gallery/<int:id>',GalleryUpdate.as_view(),name="gallery-edit"),
    path('delete-gallery/<int:id>',GalleryDelete.as_view(),name="gallery-delete"),
    #Authentication Section
    path('reset-password/',auth_views.PasswordResetView.as_view(template_name="authenticate/password_reset.html"),name="reset_password"),
    path('reset-password-sent/',auth_views.PasswordResetDoneView.as_view(template_name="authenticate/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="authenticate/password_reset_form.html"),name="password_reset_confirm"),
    path('reset-password-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="authenticate/password_reset_done.html"),name="password_reset_complete")

]
