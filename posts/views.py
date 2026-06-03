from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer