from django.contrib import admin
from menu.models import Recipe


admin.site.site_header = 'Restaurant Manager Admin Panel'
admin.site.register(Recipe)
