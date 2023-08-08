# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from .models import Author
from authentication.models import CustomUser
from order.models import Order
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .forms import BookCreateForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
@login_required
def books_page(request):
    user=CustomUser.objects.all
    book=Book.objects.all()
    try:
        if request.POST['parameter']==None or not request.POST['value']: 
            book=Book.objects.all()            
        elif request.POST['parameter']=="authors":
            book=Book.objects.filter(authors=request.POST['value']).values()
        elif request.POST['parameter']=="title":
            book=Book.objects.filter(name=request.POST['value']).values()
        elif request.POST['parameter']=="count":
            book=Book.objects.filter(count=request.POST['value']).values()
        

    except (MultiValueDictKeyError):
        book=Book.objects.all()
        
    return render(request, template_name='book/basik.html',
                  context={'books': book, 'user': user})

def book_add_page(request):
    user=CustomUser.objects.all
    book=Book.objects.all()
    try:
        if request.POST['user']:
            all_order=Order.objects.all()
            book=[]
            for elem in all_order:
                if elem.user.id==int(request.POST['user']):
                    book.append(elem.book)
    except (MultiValueDictKeyError):
        book=Book.objects.all()
    return render(request, template_name='book/basik.html',
                  context={'books': book, 'user': user})


@login_required
def book_detail(request, book_id):
    orders=Order.objects.all()
    not_avaliable=0
    for elem in orders:
        if elem.end_at==None and elem.book.id==book_id:
            not_avaliable+=1
    
    authors=Author.objects.all()
    book=Book.objects.get(id=book_id)
    book_authors=book.authors.all()
    avaliable=book.count-not_avaliable
    return render(request, template_name='book/book.html',
                  context={'book': Book.get_by_id(book_id), 'authors':authors, 'book_authors':book_authors, 'avaliable':avaliable})


@login_required
def add_author(request, book_id):
    author_id = request.POST["author"]
    book = Book.objects.get(id=book_id)
    book.authors.add(Author.objects.get(id=author_id))
    book.save()
    return render(
        request,
        template_name="book/book.html",
        context={
            "book": Book.get_by_id(book_id),
            "authors": Author.objects.all(),
            "book_authors": book.authors.all(),
        },
    )

"""
def add_book(request):
    return render(
        request,
        template_name="book/add_book.html",
        context={"authors": Author.objects.all()},
    )
"""

def new_book(request):
    name = request.POST["name"]
    description = request.POST["description"]
    count = request.POST["count"]
    authors = request.POST["authors"]
    if authors == "None":
        book = Book.create(name=name, description=description, count=count)
        book.save()
    else:
        book = Book.create(name=name, description=description, count=count)
        book.save()
        book.authors.add(Author.objects.get(id=authors))
        book.save()
    return books_page(request)

class BookCreateView(CreateView):
    template_name = 'book/book-create.html'
    form_class = BookCreateForm
    
    # def get(self, request, *args, **kwargs):
    #     context = {'form': BookCreateForm()}
    #     return render(request, 'book/book-create.html', context)

    # def post(self, request, *args, **kwargs):
    #     form = BookCreateForm(request.POST)
    #     if form.is_valid():
    #         book = form.save()
    #         book.save()
    #         return HttpResponseRedirect(reverse_lazy('book:book_detail', args=[book.id]))
    #     return render(request, 'book/book-create.html', {'form': form})

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

    def get(self, request, pk):
        context = {'form': BookCreateForm(instance=Book.objects.get(id=pk))}
        return render(request, 'book/book_update_form.html', context)

    def post(self, request, pk):
        form = BookCreateForm(request.POST, instance=Book.objects.get(id=pk))
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect(reverse_lazy('book:book_detail', args=[book.id]))

    