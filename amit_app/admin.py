from django import forms
from django.contrib import admin
from .models import GalleryCategory, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 5  # Number of empty forms you want to show

class GalleryCategoryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]

admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(GalleryImage)