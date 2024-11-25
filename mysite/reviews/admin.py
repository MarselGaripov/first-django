from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('full_name', 'email')