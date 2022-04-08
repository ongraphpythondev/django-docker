from django.contrib import admin
from .models import Scraper

@admin.register(Scraper)
class ScraperAdmin(admin.ModelAdmin):
    list_display = ['url']
    search_fields = ['url']