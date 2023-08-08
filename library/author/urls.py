from django.urls import path
from . import views
from library.functions import deny_non_librarian


app_name = 'author'

urlpatterns = [
    path("", deny_non_librarian(views.AuthorPage.as_view()), name='author'),
    path("<int:pk>", deny_non_librarian(views.AuthorDetails.as_view()), name='details'),
    path("<int:author_id>/remove", deny_non_librarian(views.remove_author), name='remove_author'),
    path("new/", deny_non_librarian(views. AuthorCreateView.as_view()), name='add_author'),
    #path("submit/", deny_non_librarian(views.submit_add_author), name='submit_new_author'),
    path("edit/<pk>", deny_non_librarian(views.AuthorUpdate.as_view()), name='edit')
]
