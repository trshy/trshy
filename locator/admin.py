from django.contrib import admin

# Register your models here.
from .models import Trashcan


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["latitude", "longitude"]
    list_display_links = ["latitude"]

    class Meta:
        model = Trashcan


admin.site.register(Trashcan, PostModelAdmin)
