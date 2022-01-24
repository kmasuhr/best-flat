# Create your views here.
from django.views.generic import TemplateView

from flats_ui.viewer.models import FlatOffer


class EmailDebugView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        queryset = FlatOffer.objects.filter(is_latest=True, last_floor=True)
        query_filter = kwargs.get('filter', None)

        if query_filter == 'favourite':
            queryset = queryset.filter(favourite=True)
        elif query_filter == 'ignored':
            queryset = queryset.filter(ignore=True)
        # if query_filter == 'new-offers':
        #     queryset = queryset.filter(crea)
        else:
            queryset = queryset.filter(ignore=False)

        return {'flats': queryset.order_by('price')}
