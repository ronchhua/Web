from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Post

from . serializers import PostSerializer

@api_view(['GET'])
def api(response):

    display_api_urls = {

        'Posts':'post-list/',
        'View all the Posts': 'post-detail/<str:pk>/',
        'Create' : 'post-create/',
        'Update' : 'post-update/<str:pk>/',
        'Delete' : 'post-delete/<str:pk>/',

    }

    return Response(display_api_urls)

@api_view(['GET'])
def postList(request):
    posts = Post.objects.all().order_by('-id')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def postDetail(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
            serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def postUpdate(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=posts, data=request.data)

    if serializer.is_valid():
            serializer.save()

    return Response(serializer.data)
    
@api_view(['DELETE'])
def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    
    post.delete()

    return Response("It has been deleted")    