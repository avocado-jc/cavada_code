
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name='home.html'
    context_object_name ='lastest_blog_list'
   
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name='post_new.html'
    fields = ['title', 'body']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class BlogEditView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name='post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name='post_delete.html'
    success_url = reverse_lazy('post:home')

