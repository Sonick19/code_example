# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:00:39 2023

@author: Sonya
"""

from django.urls import path
from . import views
app_name = 'book'


urlpatterns = [
    path("", views.books_page, name='book_main_page'),
    path("<int:book_id>/", views.book_detail, name='book_detail'),
    path("book/add_author/<int:book_id>/", views.add_author, name='add_author'),
    #path("book/add_book/", views.add_book, name='add_book'),
    path("book/new_book/", views.new_book, name='new_book'),
    path("book_add_page/", views.book_add_page, name='book_add_page'),
    path("book/add_book/", views.BookCreateView.as_view(), name='add_book'),
    path("edit/<pk>/", views.BookUpdate.as_view(), name='edit'),
]
