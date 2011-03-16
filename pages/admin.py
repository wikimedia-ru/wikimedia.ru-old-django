from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from pages.models import Page, PageFile
#from files.models import File



class PageFileInline(admin.TabularInline):
        model = PageFile


class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'extend_title', 'section', 'url', 'old_url', 'active', 'text')
        }),
        #(_('Attached files'), {
        #    'fields': ()
        #}),
    )
    inlines = (PageFileInline,)

    list_display = ['title', 'section', 'url', 'active']
    ordering = ['section', 'url']


admin.site.register(Page, PageAdmin)

