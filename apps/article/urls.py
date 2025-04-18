from django.urls import path
from .views import article_detail, article_list

app_name = 'article'

urlpatterns = [
    path('', article_list, name='list'),
    path('detail/', article_detail, name='detail'),
]