from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-id')
    return render(request, 'mysite/post_list.html', {'posts': posts})
