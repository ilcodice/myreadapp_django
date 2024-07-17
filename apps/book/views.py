from django.shortcuts import render
from django.http import HttpResponse
from . import models 

# Create your views here.
def book_detail(request, isbn):
    book = models.Book.objects.get(pk=isbn)

    context = {
        "book": book,

    }
    return render(request, 'book_detail.html', context)

def book_post(request):
    return render(request, 'post.html')