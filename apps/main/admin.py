from django.contrib import admin
from .models import Feedback, Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'email', 'created_at')
    list_display_links = ('id', 'name', 'subject')
    search_fields = ('name', 'subject')
    date_hierarchy = 'created_at'



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'created_at')
    list_display_links = ('id', 'name', 'position')
    search_fields = ('name', 'position')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
