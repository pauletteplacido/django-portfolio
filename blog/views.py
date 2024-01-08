from django.shortcuts import render, get_object_or_404
from moviepy.editor import VideoFileClip
from .models import Posts
from django.contrib.humanize.templatetags import humanize
from django.utils import timezone


def index(request):
    return render(request, 'index.html')


def render_posts(request):
    posts = Posts.objects.all().order_by('-id')
    current_time = get_current_time()
    for post in posts:
        post.created_at = current_time
        post.save()
    return render(request, 'posts.html', {'posts': posts, 'current_time': current_time})


def get_current_time():
    return humanize.naturaltime(timezone.now())


def post_detail(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})
