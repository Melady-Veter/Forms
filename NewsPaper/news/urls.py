from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('admin', admin.site.urls),
    path('pages', include('django.contrib.flatpages.urls')),
    path('',PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='new'),
    path('search', PostSearch.as_view(), name='search'),
    path('create', PostCreateView.as_view(), name='create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='create'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]