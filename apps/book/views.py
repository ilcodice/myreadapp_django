from django.shortcuts import render
from django.http import HttpResponse
from . import models 

# Create your views here.
def book_detail(request, isbn):
    book = models.Book.objects.get(pk=isbn)

    context = {
        "book": book,
        "tags": ', '.join(str(tag) for tag in book.tags.all()),
        "authors": ', '.join(str(author) for author in book.authors.all())

    }
    return render(request, 'book_detail.html', context)
