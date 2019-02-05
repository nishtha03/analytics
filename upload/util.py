from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django import template
import io
from io import StringIO
import urllib,  base64

register = template.Library()


def render_to_pdf(template_src, context_dict={}):
    dot_data = StringIO()
    template = get_template(template_src)
    html  = template.render(context_dict)

    result = BytesIO()
    links = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), dest=result, link_callback=links)
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), dest=result,link_callback=links)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
    if url.startswith("http"):
        image = io.BytesIO(urllib.urlopen(url).read())
        return 'data:image/png;base64,' + base64.b64encode(image.read())

    return url
