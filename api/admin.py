from django.contrib import admin
from .models import UrineStripImage

@admin.register(UrineStripImage)
class UrineStripImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('id',)

# Alternatively, you can use the simpler syntax without the decorator:
# admin.site.register(UrineStripImage)
