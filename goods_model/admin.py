from django.contrib import admin
from .models import GoodsMod,CategoryMod,PhotoGoods

class CategorySlug(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ImageProduct(admin.TabularInline):
    model = PhotoGoods

class YourModelAdmin(admin.ModelAdmin):
    inlines = [ImageProduct]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(GoodsMod, YourModelAdmin)

admin.site.register(CategoryMod,CategorySlug)
