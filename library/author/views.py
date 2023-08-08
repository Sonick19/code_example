from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Author
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from book.models import Book
from django import forms
from .forms import AuthorCreateForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


class AuthorPage(ListView):
    template_name = "author/author.html"
    model = Author
    context_object_name = 'authors'
    ordering = 'surname'


class AuthorDetails(DetailView):
    template_name = "author/author_details.html"
    context_object_name = 'author'
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['books'] = Book.objects.filter(authors=author)
        return context


def remove_author(request, author_id):
    if request.method == 'POST':
        try:
            author = Author.objects.get(pk=author_id)
            books_authors = Book.objects.filter(authors=author)
        except Author.DoesNotExist:
            raise Http404("Question does not exist")
        if len(books_authors) == 0:
            author.delete()
        return HttpResponseRedirect(reverse('author:author'))


#def add_author(request):
    #return render(request, template_name='author/author_create.html')
    
class AuthorCreateView(CreateView):
    template_name = 'author/author_create.html'
    form_class = AuthorCreateForm

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'

    def get(self, request, pk):
        context = {'form': AuthorCreateForm(instance=Author.objects.get(id=pk)), 'author': Author.objects.get(id=pk)}
        return render(request, 'author/author_update_form.html', context)

    def post(self, request, pk):
        form = AuthorCreateForm(request.POST, instance=Author.objects.get(id=pk))
        if form.is_valid():
            author = form.save()
            author.save()
        return HttpResponseRedirect(reverse('author:details', args=[author.id]))

# def submit_add_author(request):
#     if request.method == 'POST':
#         name = request.POST['author_name']
#         surname = request.POST['author_surname']
#         patronymic = request.POST['author_patronymic']
#         try:
#             author = Author.create(name, surname, patronymic)
#             author.save()
#         except ValueError as error:
#             HttpResponse(error)
#         return HttpResponseRedirect(reverse('author:author'))

