from django.contrib import admin
from .models import Author , Genre , Book , BookInstance

#  register 後可直接在 admin 添加 record
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Genre)


class BooksInline(admin.TabularInline):
    model = Book
    
# se the @register decorator to register the models (this does exactly the same thing as the admin.site.register() syntax
# customize  the author interface in admin page 
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    
    # change field order  &  horizontally or vertically in detail view 
    fields = ['first_name','last_name', ('date_of_birth' , 'date_of_death')]
    inlines = [BooksInline]

    

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author' , 'display_genre')
    
    # Inline editing of associated records
    inlines = [BooksInstanceInline]

    



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','id','status', 'due_back')
    list_filter = ('status', 'due_back')

    # Sectioning the detail view
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

    pass
    


