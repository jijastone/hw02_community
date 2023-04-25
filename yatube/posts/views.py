from django.shortcuts import render, get_object_or_404

from .models import Post, Group

COUNT_POST = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:COUNT_POST]\
        .select_related('group')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group.all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
