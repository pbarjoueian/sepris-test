from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField


class BaseProperties(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Publicaition(BaseProperties):
    name = models.CharField(max_length=64, null=False)
    phone_number = PhoneField(blank=True, help_text='phone number')
    address = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.name


class Author(BaseProperties):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    nick_name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.last_name


class Book(BaseProperties):
    title = models.CharField(max_length=100, unique=True)
    page_number = models.IntegerField(default=0)
    publication_year = models.IntegerField(
        default=2020)  # Better to use DateField instead
    published_by = models.ForeignKey(Publicaition, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
