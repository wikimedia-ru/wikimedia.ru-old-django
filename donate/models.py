from django.utils.translation import ugettext_lazy as _
from django.db import models



class Donation(models.Model):
    icon = models.ImageField(upload_to='donations', blank=True, null=True, verbose_name=_("Icon"))
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    anchor = models.SlugField(max_length=50, verbose_name=_("Anchor"))
    color = models.CharField(max_length=20, verbose_name=_("Background color"))
    order = models.PositiveIntegerField(verbose_name=_("Order"))
    active = models.BooleanField(default=True, verbose_name=_("Active"))

    METHOD_CHOICES = (
        ('get', 'GET'),
        ('post', 'POST'),
    )
    form_method = models.CharField(max_length=4, choices=METHOD_CHOICES, default='get', verbose_name=_("Form method"))
    form_url = models.URLField(verify_exists=False, blank=True, null=True, max_length=250, verbose_name=_("Form submit URL"))

    phone_id = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Phone field id"))
    amount_id = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Amount field id"))
    submit_text = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Submit button text"))

    text = models.TextField(blank=True, verbose_name=_("HTML text"))
    footnote = models.TextField(blank=True, verbose_name=_("Footnote"))
    hidden = models.TextField(blank=True, verbose_name=_("Hidden fields and scripts"))
    
    
    def __unicode__(self):
        return self.title


