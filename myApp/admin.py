from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class PersonAdmin(admin.ModelAdmin):
    list_display = ('email','user_name','phone_number')
    list_filter = ('email','user_name',)
    search_fields = ('user_name',)
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(Person, PersonAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('writer','date')
    list_filter = ('writer','date',)
    search_fields = ('writer',)
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(Article, ArticleAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('owner','text','date')
    list_filter = ('owner','text',)
    search_fields = ('owner',)
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer','owner_id','owner_group','text','date')
    list_filter = ('writer','owner_id','owner_group')
    search_fields = ('writer',)
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(Comment, CommentAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('liker','owner_id','owner_group','date')
    list_filter = ('liker','owner_id','owner_group')
    search_fields = ('liker',)
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(Like, LikeAdmin)

