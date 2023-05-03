from django.urls import path
from .views import BookListView, BookDetailView, GenreView, AddCommentView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name = 'books_list'),
    path('detail/<slug:slug>/', BookDetailView.as_view(), name = 'book_detail'),
    path('genre/<slug:slug>/', GenreView.as_view(), name = 'genre'),
    path('<slug:slug>/reviews/', AddCommentView.as_view(), name = 'reviews'),
]