from django.db import models

class GalleryCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery_images/')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

