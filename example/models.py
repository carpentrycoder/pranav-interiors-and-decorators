from django.db import models

class HostedImage(models.Model):
    image_url = models.URLField(max_length=500, verbose_name="Image URL")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.pk}: {self.image_url}"


