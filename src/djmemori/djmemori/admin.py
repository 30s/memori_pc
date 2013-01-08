from django.contrib import admin

from djmemori.models import ScanPath, Photo


class ScanPathAdmin(admin.ModelAdmin):
    list_display = ('path', )


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('root', 'path', 'date_taken', 'width', 'height',
                    'make', 'model', 'latitude', 'longitude')


admin.site.register(ScanPath, ScanPathAdmin)
admin.site.register(Photo, PhotoAdmin)

