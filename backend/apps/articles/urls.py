from django.urls import path
from .views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView, CategoryListCreateView

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='articles_list_create'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article_retrieve_update_destroy'),
    path('categories/', CategoryListCreateView.as_view(), name='categories_list_create'),
]
