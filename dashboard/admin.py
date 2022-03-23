from django.contrib import admin
from .models import BuildResume, TemplateName
from django.utils.html import format_html


class BuildResumeAdmin(admin.ModelAdmin):

    readonly_fields = ['created_date', 'updated_date']

    def thumbnail(self, object):
        return format_html("<img src='{}' style='width:50px;border-radius:50px;' />".format(object.profile_photo.url))
    

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'resume_title', 'email',)
    list_display_links = ('id', 'thumbnail', 'resume_title', 'email')


class TemplateNameAdmin(admin.ModelAdmin):
    list_display = ('id', "user_id", "email", "defualt_template_name")
    list_display_links = ('id', "user_id", "email", "defualt_template_name")


admin.site.register(BuildResume, BuildResumeAdmin)
admin.site.register(TemplateName, TemplateNameAdmin)
 