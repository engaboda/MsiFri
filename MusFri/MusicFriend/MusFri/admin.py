from django.contrib import admin
from music.models import Album,Song,User
# Register your models here.


class ModelAdminForm(admin.ModelAdmin):
    list_display = ["album_title","artist" ]
    list_editable = ["album_title"]
    list_filter = ["artist"]
    search_fields = ["artist" , "album_title"]
    class Meta:
        model = Album


admin.site.register(Album,ModelAdminForm)
admin.site.register(Song)
admin.site.register(User)
