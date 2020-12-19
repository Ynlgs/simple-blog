import markdown
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Post, Category, Tag
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


'''
def index(request):
    # return HttpResponse("欢迎访问我的博客首页!")
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
'''

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify)
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})

'''
从 django.shortcuts 模块导入的 get_object_or_404 方法，其作用就是当传入的 pk 对应的 Post 在数据库存在时，
就返回对应的 post，如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
'''


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    cate = get_object_or_404(Category, pk=pk)
    # post_list = Post.objects.filter(category=cate).order_by('-created_timed')
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})