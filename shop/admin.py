from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'category')
    readonly_fields = ("get_image",)
    search_fields = ('name', 'price', 'category')
    fields = ('name', 'description', 'price', 'image', 'category', 'get_image')
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    list_display_links = ("title",)
