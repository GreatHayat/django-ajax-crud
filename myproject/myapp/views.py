from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Book
from .forms import BookForm
# Create your views here.


def book_list(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "myapp/book_list.html", context)


def book_create(request):
    data = dict()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data['is_valid_form'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string(
                'includes/partial_book_list.html', {"books": books})
        else:
            data['is_valid_form'] = False
    else:
        form = BookForm()
    context = {"form": form}
    data['html_form'] = render_to_string(
        "includes/book_create_form.html", context, request=request)
    return JsonResponse(data)
