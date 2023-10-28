from django.urls import path

from .views import PostsView, PostCreateView, PostGetView, CategoryView, CategoryCreateView, TagsView, TagCreateView

urlpatterns = [
    path('all/', PostsView.as_view()),
    path('add/', PostCreateView.as_view()),
    path('<int:post_id>/', PostGetView.as_view()),
    # path('<int:post_id>/edit/', PostEditDeleteView.as_view())
    path('category/', CategoryView.as_view()),
    path('category/add/', CategoryCreateView.as_view()),
    path('tags/', TagsView.as_view()),
    path('tags/add/', TagCreateView.as_view())
]
