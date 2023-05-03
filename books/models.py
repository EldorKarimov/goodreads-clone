from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from users.models import CustomUser

class Book(models.Model):
    languages = [
        ('english', 'english'),
        ('russian', 'russian'),
        ('uzbek', 'uzbek'),
        ('french', 'french')
    ]
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images/books')
    isbn = models.CharField(max_length=20, blank=True)
    format = models.CharField(max_length=60)
    publish_time = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True
    )
    is_published = models.BooleanField(default=False)
    language = models.CharField(max_length=20, choices=languages, default='english')
    author = models.ManyToManyField('Author', related_name="book_author")
    genre = models.ManyToManyField('Genre')

    class Meta:
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    genre = models.ManyToManyField('Genre', related_name='author_genre')
    website = models.CharField(max_length=128, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField()

    def __str__(self):
        return self.user.username
