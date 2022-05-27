from django.contrib import admin
from .models import Location,Category,Image

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)
