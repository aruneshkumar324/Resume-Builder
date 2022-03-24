from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'email', 'feature', 'feedback')

    list_display_links = ('id', 'user_id', 'email', 'feature', 'feedback')


admin.site.register(Feedback, FeedbackAdmin)