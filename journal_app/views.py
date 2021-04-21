from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'journal_app/home.html', context)

def search_articles(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        search_title = Post.objects.filter(title__icontains=search)
        search_date_posted = Post.objects.filter(date_posted__icontains=search)
        print(search_date_posted)
        # post = search_title.union(search_date_posted)
        search_author = Post.objects.filter(author__username__icontains=search)
        post = search_title.union(search_author,search_date_posted)
        # post = Post.objects.filter(title__icontains=search)
        return render(request,'journal_app/search_articles.html',{'post':post})


class PostListView(ListView):
    model = Post
    template_name = 'journal_app/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'journal_app/user_posts.html'  
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','author','published_date','created_date','updated_date','slug','status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/' 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        print(post)
        print(self.request.user)
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'journal_app/about.html', {'title': 'About'})
