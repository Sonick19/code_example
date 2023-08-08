from django.contrib import admin

from .models import Book

#admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display=('id', 'name', 'display_authors', 'description', 'count')
    def display_authors(self, obj):
        return ', '.join([f"{author.surname} {author.name}" for author in obj.authors.all()])
    list_filter=('id', 'name', 'authors')
    fieldsets=[
        (
            None,
            {
                "fields": [("name", "authors")],
            },
        ),
        (
            "Avaliability",
            {
                "fields": ["count"],
                
            },
        ),
    ]
    
admin.site.register(Book, BookAdmin)