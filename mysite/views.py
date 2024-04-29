from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


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
