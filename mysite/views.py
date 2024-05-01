from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.


def post_list(request):
    posts = Post.objects.filter(
        created_date__lte=timezone.now()).order_by('-id')
    return render(request, 'mysite/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mysite/post_detail.html', {'post': post})


def who_made(request, who):
    title = Post.objects.get(title=who)
    return render(request, 'mysite/post_who.html', {'title': title})


def post_new(request):
    if request.method == "Post":
        print("ello")
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mysite/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'mysite/post_edit.html', {'form': form})
