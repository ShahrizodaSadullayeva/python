from django.contrib.admin.templatetags.admin_list import pagination
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_GET

from blog2.forms import FormComment
from blog2.models import Book, Comment, Video, Menu, Menu_part


@login_required(login_url='blog3:signup')
def python(request):
    books = Book.objects.all()

    menus = Menu.objects.all()

    menu_parts = Menu_part.objects.all()
    context = {
        'book': books,
        'menu': menus,
        'menu_part': menu_parts,
    }
    return render(request, 'blog2/python.html', context)


@require_GET
def search_book(request):
    book_query = request.GET.get('query_book')
    book_set = Book.objects.filter(name__icontains=book_query)
    context = {
        "book_search": book_set,
    }

    return render(request, 'blog2/search_book.html', context)


def book(request):
    books = Book.objects.all()
    book_count = books.count()
    p = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_objects = p.get_page(page_number)

    context = {
        'book': page_objects,
        'book_count': book_count,
    }
    return render(request, 'blog2/book.html', context)


@require_GET
def search_video(request):
    video_query = request.GET.get('query_video')
    video_set = Video.objects.filter(name__icontains=video_query)
    context = {
        "video_search": video_set,
    }

    return render(request, 'blog2/search_video.html', context)


def video(request):
    videos = Video.objects.all()
    video_count = videos.count()

    p = Paginator(videos, 6)
    page_number = request.GET.get('page')
    page_objects = p.get_page(page_number)

    context = {
        "video": page_objects,
        "video_count": video_count,
    }
    return render(request, 'blog2/video.html', context)


def comment(request):
    comments = Comment.objects.all()

    enter_comments = FormComment(request.POST)
    if request.POST:
        enter_comments = FormComment(request.POST)
        if enter_comments.is_valid():
            form_comment = enter_comments.save(commit=True)
            form_comment.post = Comment.objects.all()
            form_comment.save()

            return redirect('blog2:comment')

    context = {
        'comment': comments,
        'enter_comment': enter_comments,
    }
    return render(request, 'blog2/comment.html', context)


def run(request):
    return render(request, 'blog2/Run.html')
