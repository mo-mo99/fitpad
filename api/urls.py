from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('posts/', views.posts_list, name="show-post"),
    path('post/<pk>', views.get_post, name="get-post"),
    path('create-post', views.create_post, name="post-create"),
    path('update-post/<pk>', views.update_post, name="post-update"),
    path('delete/<pk>', views.delete_post, name="post-delete"),
    path('show-users/', views.user_view, name="users-view"),
    path('edit-user/<pk>', views.edit_user, name="edit-user"),
    path('create-user/',views.create_user, name="create-user"),
    path('delete-user/<pk>', views.delete_user, name="delete-user"),
    path('article', views.ArticleView.as_view(), name='article'),
    path('article/<pk>', views.SingleArticleView.as_view(), name="single-article-view")
]
