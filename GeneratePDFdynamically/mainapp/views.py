from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS

'''
1. render_to_string - https://docs.djangoproject.com/en/3.2/topics/templates/#django.template.loader.render_to_string

2. Content-Disposition - https://docs.djangoproject.com/en/3.2/ref/request-response/#telling-the-browser-to-treat-the-response-as-a-file-attachment
'''
'''
1. render_to_string() loads a template like get_template() and calls its render() method immediately 
   and we need this because we need to render html so that we can convert it to pdf

2. Installing weasyprint https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows

3. If you are getting error even on installing GTK3 then please uninstall GTK3 and again install it in "<instdir>/lib"
   directory. Everythong will work fine. https://stackoverflow.com/a/63464139 (No need of GTK2)

4. How to use weasyprint https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#quickstart

'''
class Order:
   id = 56

def show_pdf(request, order_id=56):
    # order = get_object_or_404(Order, id=order_id)
    order = Order()
    html = render_to_string('pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment ; filename=order_{order.id}.pdf' # With "attachment" key PDF will only be downloaded to the system
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf' # Only PDF will open in browser
    HTML(string=html).write_pdf(response)
    # HTML(string=html).write_pdf(response, stylesheets=[CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response

def download_pdf(request, order_id=56):
    order = Order()
    html = render_to_string('pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment ; filename=order_{order.id}.pdf' # With "attachment" key PDF will only be downloaded to the system
    HTML(string=html).write_pdf(response)
    # HTML(string=html).write_pdf(response, stylesheets=[CSS(settings.STATIC_ROOT + 'css/pdf.css')]) # If you want to use css file present in static folder
    return response    