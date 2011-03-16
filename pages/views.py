'''
import re
import urllib
from hyphenator import Hyphenator
'''

from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Lexer, TOKEN_BLOCK
from django.http import HttpResponsePermanentRedirect

from pages.models import Page
from donate.views import donations_list



enabled_tags = {
    'donations': donations_list
    }


def page(request, url, section = None):
    
    try:
        page = Page.objects.get(url = url, section__url = section)
    except:
        if (section == None):
            page = get_object_or_404(Page, old_url = url)
        else:
            page = get_object_or_404(Page, old_url = section + '/' + url)
        return HttpResponsePermanentRedirect('/' + page.url)
    
    text = ''
    
    # Template tags
    for token in Lexer(page.text, 'shell').tokenize():
        if token.token_type == TOKEN_BLOCK and token.contents in enabled_tags:
            text += enabled_tags[token.contents](request)
        else:
            text += token.contents
    
    '''
    url = "http://www.typograf.ru/webservice/"
    params = urllib.urlencode({
        'chr': 'UTF-8',
        'minus-sign': '&minus;',
        'tags': '0',
        'paragraph': '0',
        'newline': '0',
        'dos-text': '1',
        'acronym': '0',
        'symbols': '1',
        
        'text': text.replace('\n', ' ').encode('utf-8'),
        })
    f = urllib.urlopen(url, params)
    text = f.read().decode('utf-8')
    
    h = Hyphenator('/usr/share/myspell/dicts/hyph_ru_RU.dic', 4, 4)
    text = re.sub(r'\s&shy;|&shy;\s', ' ', h.inserted(text, '&shy;')).replace('&shy;', u'\u00AD')
    '''

    return render_to_response('pages/index.html', {
        'title': page.title,
        'text': text,
        }, context_instance=RequestContext(request))
