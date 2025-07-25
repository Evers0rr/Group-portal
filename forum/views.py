from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import PostForm, CommentForm
from .models import Post

def forum_home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'forum/forum_home.html', {'posts': posts})

@user_passes_test(lambda u: u.is_staff)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect('forum_home')
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.order_by('created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'forum/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

@user_passes_test(lambda u: u.is_staff)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('forum_home')
    return render(request, 'forum/confirm_delete.html', {'post': post})
