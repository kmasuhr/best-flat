# Create your views here.
from datetime import timedelta

from django.utils import timezone
from django.views.generic import TemplateView

from flats_ui.viewer.models import FlatOffer


class EmailDebugView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        queryset = FlatOffer.objects.filter(is_latest=True, last_floor=True)
        query_filter = kwargs.get('filter', None)

        if query_filter == 'favourite':
            queryset = queryset.filter(favourite=True).order_by('price')
        elif query_filter == 'ignored':
            queryset = queryset.filter(ignore=True).order_by('price')
        elif query_filter == 'new-offers':
            today = timezone.now()
            queryset = queryset.filter(created_on__gte=today - timedelta(days=1))
            queryset = queryset.order_by('-created_on')
        else:
            queryset = queryset.filter(ignore=False, favourite=False).order_by('price')

        return {'flats': queryset}
