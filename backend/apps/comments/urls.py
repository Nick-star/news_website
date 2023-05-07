from django.urls import path
from .views import CommentListCreateView, CommentRetrieveUpdateDestroyView

urlpatterns = [
    path('comments/', CommentListCreateView.as_view(), name='comments_list_create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment_retrieve_update_destroy'),
]
