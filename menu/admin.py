from django.contrib import admin

from menu.models import MenuItem



class MenuItemAdmin(admin.ModelAdmin):
    fields = ['text', 'url', 'rel', 'order']
    list_display = ['text', 'url', 'rel']
    ordering = ['order']

admin.site.register(MenuItem, MenuItemAdmin)

