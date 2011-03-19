import re

from django.template.loader import render_to_string
from django.template import RequestContext

from donate.models import Donation



def donations_list(request):
    d_list = Donation.objects.order_by('order')
    '''
    for d_item in d_list:
        if d_item.phone_id.find('=') >= 0:
            d_item.phone_tpl = '<span class="d-tpl">' + re.sub(r'\[(?P<id>[^\[\]=]+)=(?P<len>[^\[\]=]+)\]', '<input type="text" name="\g<id>" maxlength="\g<len>" size="\g<len>" placeholder="" pattern="\d{\g<len>}" required="required" />', d_item.phone_id) + '</span>'
        if d_item.amount_id.find('=') >= 0:
            d_item.amount_tpl = '<span class="d-tpl">' + re.sub(r'\[(?P<id>[^\[\]=]+)=(?P<len>[^\[\]=]+)\]', '<input type="text" name="\g<id>" maxlength="\g<len>" size="\g<len>" placeholder="" required="required" />', d_item.amount_id) + '</span>'
    '''
    
    return render_to_string('donate/donations_list.html', {
        'donations': d_list,
        }, context_instance=RequestContext(request))
