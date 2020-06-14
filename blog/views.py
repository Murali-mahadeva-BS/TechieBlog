from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q  # new


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class PostsPageView(generic.ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


class ProfilePageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'
    login_url = 'account_login'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'post_create.html'


class SearchResultListView(generic.ListView):
    model = Post
    context_object_name = 'search_result'
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_result = 0
        if query:
            search_result = Post.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query))
            return search_result
        return search_result
