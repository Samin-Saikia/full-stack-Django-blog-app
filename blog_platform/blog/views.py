from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import PostForm


def home(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'blog/home.html', {
        'posts': posts,
        'categories': categories
    })
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})
def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(
        category=category,
        status='published'
    ).order_by('-created_at')

    return render(request, 'blog/category_posts.html', {
        'category': category,
        'posts': posts
    })

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = Post.objects.filter(
        tags=tag,
        status='published'
    ).order_by('-created_at')

    return render(request, 'blog/tag_posts.html', {
        'tag': tag,
        'posts': posts
    })
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('blog:home')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Only the author or superuser can edit
    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admins can delete posts.")

    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('blog:home')        
@login_required
def my_posts(request):
    # Get posts written by the logged-in user
    posts = Post.objects.filter(author=request.user).order_by('-created_at')

    return render(request, 'blog/my_posts.html', {'posts': posts})    