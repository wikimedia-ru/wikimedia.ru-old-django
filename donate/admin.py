from django.contrib import admin

from donate.models import Donation



class DonationAdmin(admin.ModelAdmin):
    fields = ['title', 'anchor', 'icon', 'color', 'order', 'form_url', 'form_method', 'phone_id', 'amount_id', 'submit_text', 'text', 'footnote', 'hidden']
    list_display = ['title', 'anchor']
    ordering = ['order']

admin.site.register(Donation, DonationAdmin)

