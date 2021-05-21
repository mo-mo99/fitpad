from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *


@login_required(login_url='entrance')
def home(request):
    posts = Post.objects.all().select_related('owner')
    visitor_followings = request.user.person.get_following
    cur_post = posts.filter(owner__in=visitor_followings)

    return render(request, 'html/MainPage.html', context={'posts': cur_post})


def sign_in(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']

            if User.objects.filter(username=user_name).exists():
                note = "username is already taken"
                context = {'note': note}
                return render(request, 'html/signin.html', context=context)
            else:

                user = User.objects.create_user(username=user_name, email=email, password=password, is_staff=False)
                user.save()
                person = Person.objects.create(user=user,user_name=user_name, email=email, password=password, phone_number=phone_number, age=age)
                person.save()


                return home(request)

    else:
        form = Registration()
        return render(request, 'html/signin.html',context={'form':form})


def log_in(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            user = authenticate(request, username=user_name, password=password)

            if user is not None:
                login(request, user)
                return home(request)
            else:
                return home(request)
                # form = LogIn()
                # return render(request, 'html/login.html', context={'form':form})
    else:
        form = LogIn()

    return render(request, 'html/login.html', context={'form': form})


def log_out(request):
    if request.method == 'GET':
        logout(request)

    return home(request)


def profile_view(request, pk):
    current_user_id = int(request.user.person.id)
    user = Person.objects.get(id=pk)
    posts = Post.objects.all().select_related("owner")
    profile_post = [p for p in posts if p.owner.id == int(pk)]
    followings = len(user.following.all())
    followers = len(user.followers.all())
    post_len = len(profile_post)
    id = int(pk)
    status = user.followers.all().filter(user_id_id =current_user_id).exists()



    return render(request, 'html/profile.html', context={'status':status,'cur': current_user_id,
                                                         'id': id,'posts': profile_post, 'followings': followings,
                                                         'followers': followers, 'post':post_len,
                                                         'owner': user})


def posting(request):
    if request.method == 'POST':
        form = Posting(request.POST, request.FILES)
        if form.is_valid():
            owner = request.user.person
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']

            new_post = Post.objects.create(owner=owner, text=text, image=image)
            new_post.save()
            return home(request)
        else:
            return home(request)
    else:
        form = Posting()
        return render(request, 'html/posting.html', context={'form': form})


def follow(request, pk):
    user = request.user.person
    s = Person.objects.get(id=pk)
    if not s.followers.all().select_related('user_id').filter(user_id=user).exists():

        following = UserFollowing.objects.create(user_id=user, following_user_id=s )
        following.save()

        return profile_view(request,pk)
    else:
        return profile_view(request,pk)


def unfollow(request, pk):
    user = request.user.person
    page_owner = Person.objects.get(id=pk)
    follow_case = UserFollowing.objects.get(user_id=user, following_user_id=page_owner)
    follow_case.delete()
    return profile_view(request, pk)


def entrance(request):
    return render(request, 'html/Entrance.html')


def show_post(request, pk):
    post = Post.objects.get(id= pk)
    comments = post.get_post_com
    likes = len(post.get_post_like)
    num_com = len(comments)
    form = Commenting()
    status = Post.objects.get(id=pk).get_post_like.filter(owner_id=pk).exists()
    return render(request, 'html/post.html', context={'status':status,'post':post, 'comments':comments, 'form': form, 'num':num_com, 'like':likes})


def add_comment(request,group, pk):
    if request.method == 'POST':
        form = Commenting(request.POST)
        if form.is_valid():
            writer = request.user.person
            text = form.cleaned_data['text']

            comment = Comment.objects.create(writer=writer, text=text, owner_group=group, owner_id=pk)
            comment.save()
            return show_post(request, pk)


def like(request, group, pk):
    visitor = request.user.person
    cur_like = Post.objects.get(id=pk).get_post_like.filter(owner_id=pk)
    if not cur_like.exists():
        new_like = Like.objects.create(liker=visitor, owner_group=group, owner_id=pk)
        new_like.save()
        return show_post(request,pk)
    else:
        cur_like.delete()
        return show_post(request,pk)


def add_article(request):
    user = request.user.person
    if request.method == 'POST':
        form = WriteArticle(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            new_article = Article.objects.create(writer=user, text=text)
            new_article.save()

            return profile_view(request,user.id)

    else:
        form = WriteArticle()
        return render(request, 'html/article.html', context={'form': form})




