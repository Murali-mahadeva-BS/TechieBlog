from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('posts/', views.PostsPageView.as_view(), name='posts'),
    path('profile/', views.ProfilePageView.as_view(), name='profile'),
    path('posts/<uuid:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('search/', views.SearchResultListView.as_view(), name='search-result'),
]
