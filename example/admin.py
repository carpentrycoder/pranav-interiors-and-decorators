from django.contrib import admin
from .models import HostedImage

@admin.register(HostedImage)
class HostedImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'uploaded_at')
    search_fields = ('image_url',)
