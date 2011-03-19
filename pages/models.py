from django.utils.translation import ugettext_lazy as _
from django.db import models



class Page(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name=_("Title"))
    extend_title = models.BooleanField(default=True, verbose_name=_("Extend default title"))
    section = models.ForeignKey('self', blank=True, null=True, limit_choices_to = {'section': None, 'title__gt': ''}, verbose_name=_("Section"))
    url = models.CharField(max_length=200, blank=True, verbose_name=_("URL"))
    old_url = models.CharField(max_length=200, blank=True, verbose_name=_("Old URL"))
    text = models.TextField(blank=True, verbose_name=_("HTML text"))
    active = models.BooleanField(default=True, verbose_name=_("Active page"))
    
    def __unicode__(self):
        return self.title


class PageFile(models.Model):
    def make_upload_path(instance, filename):
        if instance.page.section:
            if instance.page.section.url:
                return u"%s/%s/%s" % (instance.page.section.url, instance.page.url, filename)
            else:
                return u"%s/%s/%s" % ('index', instance.page.url, filename)
        else:
            if instance.page.url:
                return u"%s/%s" % (instance.page.url, filename)
            else:
                return u"%s/%s" % ('index', filename)
    
    page = models.ForeignKey('Page', verbose_name=_("Page"))
    file = models.FileField(upload_to=make_upload_path, blank=True, null=True, verbose_name=_("File"))

