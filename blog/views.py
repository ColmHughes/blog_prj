from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_home(request):
    return render(request, 'blog/index.html')
    
def view_blog(request):
    blogs = Post.objects.all()
    return render(request, 'blog/view_blog.html', {'blogs': blogs})