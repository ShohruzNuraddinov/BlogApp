from django.urls import path

from .views import CommentsView, CommentCreateView, CommentView

urlpatterns = [
    path('all/', CommentsView.as_view()),
    path('add/', CommentCreateView.as_view()),
    path('post/<int:post_id>/', CommentView.as_view())
]
