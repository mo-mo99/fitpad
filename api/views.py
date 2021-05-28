from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from myApp.models import *
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import ArticleSerializer


# class PostView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def perform_create(self, serializer):
#         owner = get_object_or_404(Person, id=self.request.data.get('owner_id'))
#         return serializer.save(owner=owner)
#
#
# class SinglePostView(RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

@api_view(['GET'])
def posts_list(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_post(request, pk):
    post = Post.objects.all().filter(id=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(status.HTTP_200_OK)


@api_view(['POST'])
def update_post(request, pk):
    post = Post.objects.filter(id=pk)
    serializer = PostSerializer(post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_post(request, pk):
    post = Post.objects.filter(id=pk)
    post.delete()

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def user_view(request):
    users = Person.objects.all()
    serializer = PersonSerializer(users, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def edit_user(request, pk):
    user = Person.objects.get(id=pk)

    serializer = PersonSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = PersonSerializer(request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_user(request, pk):
    user = Person.objects.get(id=pk)
    user.delete()

    return Response('user deleted')



class ArticleView( ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        writer = get_object_or_404(Person, id=self.request.data.get('writer_id'))
        return serializer.save(writer= writer)


class SingleArticleView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer