from django.utils.translation import ugettext_lazy as _
from django.db import models

class MenuItem(models.Model):
    text = models.CharField(max_length=100, verbose_name=_("Link text"))
    url = models.CharField(max_length=250, verbose_name=_("URL"))
    rel = models.CharField(max_length=100, blank=True, verbose_name=_("Rel attribute"))
    order = models.PositiveIntegerField(verbose_name=_("Order"))
    
    def __unicode__(self):
        return self.text

