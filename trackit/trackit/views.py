from django.views.generic import (TemplateView,)

class TestPage(TemplateView):
    template_name = 'trackit/test.html'

class ThanksPage(TemplateView):
    template_name = 'trackit/thanks.html'

class HomePage(TemplateView):
    template_name = 'trackit/index.html'
