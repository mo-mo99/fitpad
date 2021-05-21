from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('signin/', sign_in, name="sign_in"),
    path('login/', log_in, name="log_in"),
    path('', home, name="home"),
    path('logout/', log_out, name="log_out"),
    path('profile/<pk>', profile_view, name="profile"),
    path('posting/', posting, name="posting"),
    path('follow/<pk>', follow, name="following"),
    path('unfollowing/<pk>', unfollow, name="unfollow"),
    path('welcome/', entrance, name="entrance"),
    path('post/<pk>', show_post, name="show_post"),
    path('comment/<str:group>/<int:pk>', add_comment, name="add_comment"),
    path('like/<str:group>/<int:pk>', like, name="liking"),
    path('addarticle', add_article, name="add_article"),
]