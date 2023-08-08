from django.db import models
from author.models import Author
from django.urls import reverse
class Book(models.Model):
    """
        This class represents an Book. \n
        Attributes:
        -----------
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list->Author
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=128)
    description = models.CharField(blank=True, max_length=256)
    count = models.IntegerField(default=10, blank=True)
    authors =  models.ManyToManyField(Author, blank=True)
    
    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        author_list=[]
        for elem in self.authors.all():
            author_list.append(' '.join([elem.name, elem.surname]))
            
        return f" id: {self.id}, book: {self.name}, authors: {', '.join(author_list)}"
    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f"Book(id={self.id})"
    @staticmethod
    def get_by_id(book_id):
        """
        :param book_id: SERIAL: the id of a Book to be found in the DB
        :return: book object or None if a book with such ID does not exist
        """
        return Book.objects.get(id=book_id) if Book.objects.filter(id=book_id) else None
    @staticmethod
    def delete_by_id(book_id):
        """
        :param book_id: an id of a book to be deleted
        :type book_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        if Book.get_by_id(book_id) is None:
            return False
        Book.objects.get(id=book_id).delete()
        return True
    @staticmethod
    def create(name, description, count=10, authors=[]):
        """
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list->Author
        :return: a new book object which is also written into the DB
        """
        if len(name) > 128:
            return None

        book = Book()
        book.name = name
        book.description = description
        book.count = count
        book.save()
        if isinstance(authors, list):
            for elem in authors:
                book.authors.add(elem)
        else:
            book.authors=[].append(authors)
        book.save()
        return book
        book.save()
        return book
    def to_dict(self):
        """
        :return: book id, book name, book description, book count, book authors
        :Example:
        | {
        |   'id': 8,
        |   'name': 'django book',
        |   'description': 'bla bla bla',
        |   'count': 10',
        |   'authors': []
        | }
        """
        return {'id': self.id,
                'name': f'{self.name}',
                'description': f'{self.description}',
                'count': f'{self.count}',
                'authors': f'{self.authors}'}
    def update(self, name=None, description=None, count=None):
        """
        Updates book in the database with the specified parameters.\n
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        :return: None
        """
        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if count is not None:
            self.count = count

        if self.count < 0:
            self.count = 0

        self.save()

    def add_authors(self, authors):
        """
        Add  authors to  book in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """
        if (authors is not None):
            for elem in authors:
                self.authors.add(elem)
                self.save()

    def remove_authors(self, authors):
        """
        Remove authors to  book in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """
        for elem in self.authors.values():
            self.authors.remove(elem['id'])
    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all books
        """
        return list(Book.objects.all())
    def get_absolute_url(self):
        return reverse('book:book_detail', args=[self.id])