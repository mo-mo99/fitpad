from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    user_name = models.CharField(max_length=15, blank=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20 ,blank=True, null=True)
    age = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.user_name

    @property
    def get_followers(self):
        followers = self.followers.all().select_related("user_id")
        result = [i.user_id for i in followers]
        return result

    @property
    def get_following(self):
        followings = self.following.all().select_related("following_user_id")
        result = [i.following_user_id for i in followings]
        return result


class UserFollowing(models.Model):
    user_id = models.ForeignKey(Person, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(Person, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    writer = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=True)
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =''
        return url

    @property
    def get_post_com(self):
        comments = Comment.objects.all().select_related('writer').filter(owner_group='post')
        cur_cum = comments.filter(owner_id=self.id)
        return cur_cum

    @property
    def get_post_like(self):
        likes = Like.objects.all().select_related('liker').filter(owner_group = 'post')
        cur_like = likes.filter(owner_id=self.id)
        return cur_like


class Comment(models.Model):
    writer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    owner_id = models.FloatField(blank=False)
    owner_group = models.CharField(max_length=10, blank=False, null=False)
    text = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    liker = models.ForeignKey(Person, on_delete=models.CASCADE)
    owner_id = models.FloatField(blank=False)
    owner_group = models.CharField(max_length=10, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)


class Room(models.Model):
    student = models.FloatField()


