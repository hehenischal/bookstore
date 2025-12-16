from django.contrib import admin
from .models import Author, Genre, Publication, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_birth")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "color")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_establishment")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "publisher",
        "genre",
        "price",
        "stock",
        "is_in_stock",
        "published_date",
    )
    list_filter = (
        "genre",
        "publisher",
        "author",
        "published_date",
    )
    search_fields = (
        "title",
        "ISBN",
        "author__name",
        "publisher__name",
    )
    ordering = ("title",)
    list_select_related = ("author", "publisher", "genre")
    readonly_fields = ("is_in_stock",)
    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "description", "ISBN", "cover_image")
        }),
        ("Relations", {
            "fields": ("author", "publisher", "genre")
        }),
        ("Publishing", {
            "fields": ("published_date", "page_count")
        }),
        ("Inventory & Pricing", {
            "fields": ("price", "stock", "is_in_stock")
        }),
    )
