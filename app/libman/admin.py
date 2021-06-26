from django.contrib import admin

from .models import Author, Book, Publicaition


class PublicationModelAdmin(admin.ModelAdmin):
    fields = ['id', 'name', 'phone_number', 'address', 'created_by']
    list_display = ['id', 'name', 'phone_number', 'address']
    list_filter = []
    search_fields = ['id', 'name']
    exclude = []
    raw_id_fields = []
    dynamic_raw_id_fields = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    allowed_actions = []
    inlines = []


class AuthorModelAdmin(admin.ModelAdmin):
    fields = ['id', 'first_name', 'last_name', 'nick_name', 'created_by']
    list_display = ['id', 'first_name', 'last_name', 'nick_name']
    list_filter = []
    search_fields = ['id', 'first_name', 'last_name', 'nick_name']
    exclude = []
    raw_id_fields = []
    dynamic_raw_id_fields = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    allowed_actions = []
    inlines = []


class BookModelAdmin(admin.ModelAdmin):
    fields = ['id', 'title', 'page_number',
              'publication_year', 'published_by', 'author', 'created_by']
    list_display = ['id', 'title', 'page_number',
                    'publication_year', 'published_by', 'get_authors']
    list_filter = []
    search_fields = ['title', 'published_by__name', 'author__last_name',
                     'author__first_name', 'author__nick_name']
    exclude = []
    raw_id_fields = []
    dynamic_raw_id_fields = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    allowed_actions = []
    inlines = []

    def get_authors(self, obj):
        return "\n".join([p.last_name for p in obj.author.all()])


admin.site.register(Publicaition, PublicationModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Book, BookModelAdmin)
