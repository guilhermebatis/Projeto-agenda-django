from django.contrib import admin

from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'category'
    ordering = 'id',
    search_fields = 'id', 'first_name', 'last_name', 'phone'
    list_per_page = 10
    list_max_show_all = 50
    list_display_links = 'id', 'first_name',
    


@admin.register(models.Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
