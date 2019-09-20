from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone 
from django.urls import reverse 
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from datetime import datetime
from .models import Post 
from .forms import PostForm 

# Create your views here.

class PostListView(ListView):
    template_name = 'insta/home.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'insta/details.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now())
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

class PostCreateView(CreateView):
    template_name = 'insta/create.html'
    form_class = PostForm
    queryset = Post.objects.all()     #.filter(created_date__lte=timezone.now())
    #success_url = '/'
    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    template_name = 'insta/create.html'
    form_class = PostForm 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

        def form_valid(self, form):
            form.instance.author = self.request.user 
            return super().form_valid(form) 

class PostDeleteView(DeleteView):
    template_name = 'insta/delete.html'

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_success_url(self):
        return reverse('insta:post_list')

def saved_posts(request):
    posts = Post.objects.filter(saved=True)
    context = {'saved_posts': posts}
    return render(request, 'insta/saved_posts.html', context) 



# def post_create_view(request):
#     if request.method == 'POST':

#         form = PostForm(request.POST, request.FILES)

#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('/')
#     else:
#         form = PostForm()
#         context = {'form':form}
#     return render(request, 'insta/create.html', context)
