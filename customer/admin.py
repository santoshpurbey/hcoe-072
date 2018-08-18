from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_no', 'account_type', 'contact_no','address','balance', 'created', 'updated')
    list_filter = ('account_type',)
    list_per_page = 1
    list_display_links = ('name', 'account_no', 'contact_no')
    search_fields = ('name', 'account_no', 'contact_no', 'citizenship_no')
    date_hierarchy = 'created'

# admin.site.register(Profile)
