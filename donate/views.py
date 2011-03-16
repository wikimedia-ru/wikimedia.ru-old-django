from django.template.loader import render_to_string
from django.template import RequestContext

from donate.models import Donation



def donations_list(request):
    d_list = Donation.objects.order_by('order')
    
    return render_to_string('donate/donations_list.html', {
        'donations': d_list,
        }, context_instance=RequestContext(request))
