from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import GalleryCategory, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 5
    readonly_fields = ['image_preview']
    fields = ['image', 'name', 'image_preview']
    can_delete = True  # ✅ Allow image deletion

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="70" style="object-fit:cover;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'

class GalleryCategoryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]



admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(GalleryImage)
