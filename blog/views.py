from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .forms import Tag_Form, Post_Form
from .models import Post, Tag
from .utils import Detail_Object_Mixin, Create_Object_Mixin, Update_Object_Mixin, Delete_Object_Mixin
from django.db.models import Q


def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    return render(request, 'blog/posts_list.html',
                  context={'page': page, 'next_page_url': next_url, 'prev_page_url': prev_url})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class Post_Detail(Detail_Object_Mixin, View):
    model = Post
    template = 'blog/post_detail.html'


class Tag_Detail(Detail_Object_Mixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class Tag_Create(LoginRequiredMixin, Create_Object_Mixin, View):
    model = Tag_Form
    template = 'blog/tag_create.html'
    raise_exception = True


class Post_Create(LoginRequiredMixin, Create_Object_Mixin, View):
    model = Post_Form
    template = 'blog/post_create.html'
    raise_exception = True


class Tag_Update(LoginRequiredMixin, Update_Object_Mixin, View):
    model = Tag
    template = 'blog/tag_update.html'
    form_class = Tag_Form
    raise_exception = True


class Post_Update(LoginRequiredMixin, Update_Object_Mixin, View):
    model = Post
    template = 'blog/post_update.html'
    form_class = Post_Form
    raise_exception = True


class Tag_Delete(LoginRequiredMixin, Delete_Object_Mixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


class Post_Delete(LoginRequiredMixin, Delete_Object_Mixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'post_list_url'
    raise_exception = True
