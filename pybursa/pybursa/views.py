from django.shortcuts import render
from django.views.generic.base import TemplateView

# def contacts(request):
#     return render(request, 'contact.html')
import logging

logger = logging.getLogger(__name__)


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        logger.error('Some Logging')
        return {'page_title': 'Contacts - PyBursa'}
