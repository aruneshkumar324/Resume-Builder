from django.contrib import admin
from .models import BuildResume
from django.utils.html import format_html


class BuildResumeAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html("<img src='{}' style='width:50px;border-radius:50px;' />".format(object.profile_photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'email', )
    list_display_links = ('id', 'email')


admin.site.register(BuildResume, BuildResumeAdmin)