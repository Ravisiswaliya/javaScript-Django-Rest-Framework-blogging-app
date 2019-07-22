from .serializers import PostSerializer
from rest_framework.views import APIView
from django.http import Http404
from blogging.models import Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView


class PostView(APIView):
    
    # to fetch all post
    def get(self, request, format=None):
        snippets = Post.objects.all().order_by("-id")
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)
    
    # to create new post
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SinglePostView(APIView):
    
    # to get single object
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    # to fetch single object detail
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    # to delete record
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    # to update record
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(instance=post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        pass
























