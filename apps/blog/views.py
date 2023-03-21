from django.shortcuts import render, get_object_or_404
from apps.category.models import Category

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from django.db.models.query_utils import Q

from .models import Post
from .serializers import PostSerializer
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination

class BlogListView(APIView):
    def get(self, request, format=None):
        if Post.postobjects.all().exists():
            post=Post.postobjects.all()
            paginator=SmallSetPagination()
            result=paginator.paginate_queryset(post, request)
            serializer=PostSerializer(result, many=True)

            return paginator.get_paginated_response({'post':serializer.data})
        else:
            return Response({'error':'No post found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)                

class BlogListCategoryView(APIView):
    def get(self, request, category_id, format=None):
        if Post.postobjects.all().exists():
            category = Category.objects.get(id=category_id)
            post = Post.postobjects.all().filter(category=category) 

            paginator = SmallSetPagination()
            result = paginator.paginate_queryset(post, request)
            serializer = PostSerializer(result, many=True)

            return paginator.get_paginated_response({'post':serializer.data})
        else:
            return Response({'error':'No post found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PostDetailView(APIView):
    def get(self, request, post_slug, format=None):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response({'post':serializer.data}, status=status.HTTP_200_OK)

class SerchBloglogView(APIView):
    def get(self, request, search_term):
        matches = Post.postobjects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term) | Q(category__name__icontains=search_term))

        serializer = PostSerializer(matches, many=True)
        return Response({'filtered_post':serializer.date}, status=status.HTTP_200_OK)
        
