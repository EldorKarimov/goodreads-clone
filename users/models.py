from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=128, unique=True,
                              help_text=(
                                  "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
                              ),
                              error_messages={
                                  "unique": ("A user with that username already exists."),
                              },
                              )
    USERNAME_FIELD = 'username'

    picture = models.ImageField(upload_to='media/images/users', default="media/images/users/images.jpg", blank=True)

    def __str__(self):
        return self.username
