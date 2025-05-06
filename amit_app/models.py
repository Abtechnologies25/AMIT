from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
class GalleryCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery_images/')
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name if self.name else self.image.name.split("/")[-1]

@receiver(models.signals.post_delete, sender=GalleryImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)