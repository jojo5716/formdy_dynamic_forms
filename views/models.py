from django.http import HttpResponse


def render_model_form(request):
    html = "<html><body>Model form.</body></html>"

    return HttpResponse(html)
