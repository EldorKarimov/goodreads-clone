from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from .models import Book, Comment, Genre
from .forms import AddCommentForm

class BookListView(View):
    def get(self, request):
        search_book_title = request.GET.get("search_book", '')
        search_genre_book = request.GET.get("search_genre_books", '')

        if search_book_title:
            books = Book.objects.filter(title__icontains = search_book_title)
            paginator = Paginator(books, 4)
            page_num = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_num)
        else:
            books = Book.objects.all().order_by('-id')
            paginator = Paginator(books, 4)
            page_num = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_num)
        if search_genre_book:
            popular_books = Book.objects.filter(title__icontains = search_genre_book).order_by("-views")[:3]
            genres = Genre.objects.filter(name__icontains = search_genre_book)
        else:
            popular_books = Book.objects.all().order_by("-views")[:3]
            genres = Genre.objects.all()
        


        context = {
            'books':page_obj,
            'popular_books':popular_books,
            'genres':genres,
            'search_book_title':search_book_title,
            'search_genre_book':search_genre_book
        }
        return render(request, 'books/books_list.html', context)

class BookDetailView(View):
    def get(self, request, slug):
        try:
            form = AddCommentForm()
            book = Book.objects.get(slug = slug)
            context = {
                'book':book,
                'form':form
            }
            book.views += 1
            book.save()
            return render(request, 'books/book_detail.html', context)
        except ObjectDoesNotExist:
            return render(request, 'not_found.html')


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, slug):
        form = AddCommentForm(data=request.POST)
        book = Book.objects.get(slug = slug)
        if form.is_valid():
            Comment.objects.create(
                book = book,
                user = request.user,
                text = form.cleaned_data['text'],
                stars_given = form.cleaned_data['stars_given']
            )
            return redirect(reverse('books:book_detail', kwargs={'slug':book.slug}))
        else:
            return render(request, 'books/book_detail.html', {'form': form})


class GenreView(View):
    def get(self, request, slug):

        genre = Genre.objects.get(slug = slug)
        books = Book.objects.filter(genre = genre)
        genres = Genre.objects.all()
        context = {
            'genre':genre,
            'books':books,
            'genres':genres,
        }
        return render(request, 'books/genre.html', context)


