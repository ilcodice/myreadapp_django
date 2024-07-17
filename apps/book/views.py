from django.shortcuts import render
from django.http import HttpResponse
from . import models 
from .forms import PostBookForm

# Create your views here.
def book_detail(request, isbn):
    book = models.Book.objects.get(pk=isbn)

    context = {
        "book": book,

    }
    return render(request, 'book_detail.html', context)

# def book_post(request):
#     #breakpoint()
#     return render(request, 'post.html')

def book_post(request):
    # Get our form in the two states.
    # - pre-submit
    #    - http method: `GET`
    # - post-submit
    #    -- http method: `POST`

    #breakpoint()
    if request.method == 'GET':
        # pre-submit
        form = PostBookForm()
        context = {"form": form}

        return render(
            request,
            'book_post.html',
            context
        )
    elif request.method == 'POST':
        # post-submit
        data = request.POST
        form = PostBookForm(data)

        # Validation
        if form.is_valid():
            data = form.cleaned_data
            # TODO: Save to database
            # TODO: Redirect to home page




