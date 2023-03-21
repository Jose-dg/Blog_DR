from django.urls import path, include
from .views import BlogListView, BlogListCategoryView, PostDetailView, SerchBloglogView

urlpatterns = [
    path('', BlogListView.as_view()),
    path('category/<category_id>', BlogListCategoryView.as_view()),
    path('post_slug', PostDetailView.as_view()),
    path('search/<str:search_term>', SerchBloglogView.as_view()),
]
