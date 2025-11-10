from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"Profile of {self.author.name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


class Reader(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='readers')

    def __str__(self):
        return self.name
