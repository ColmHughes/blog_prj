from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import NewPostForm, EditPostForm

# Create your views here.
def blog_home(request):
    return render(request, 'blog/index.html')
    
def post_list(request):
    blogs = Post.objects.all()
    return render(request, 'blog/post_list.html', {'blogs': blogs})
    
def post_detail(request, id):
    post=get_object_or_404(Post, pk=id)
    post.read=True
    post.save
    return render(request, 'blog/post_detail.html', {'post': post})

    
def new_post(request):
    if request.method=="POST":
        form = NewPostForm(request.POST)
        message = form.save(commit=False)
        message.author = request.user
        message.save()
        return redirect('post_list')
    else:
        form = NewPostForm()
    
    return render(request, "blog/new_post.html", { 'form': form })
    
    
    
    
    
def edit_post(request, id):
    item = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        print("It's a post")
        form = EditPostForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        print("It's a get")
    
    form = EditPostForm(instance=item)
    return render(request, 'blog/edit_post.html', {'form': form})