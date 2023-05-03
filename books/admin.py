from django.contrib import admin

from .models import Book, Genre, Comment, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'format', 'publish_time', 'is_published')
    prepopulated_fields = {'slug':('title',)}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register([Comment, Author])