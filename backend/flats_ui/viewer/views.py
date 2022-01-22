# Create your views here.
from django.views.generic import TemplateView
from flats_ui.viewer.models import FlatOffer


class EmailDebugView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        return {'flats': FlatOffer.objects.filter(
            is_latest=True,
            last_floor=True,
            ignore=False,
        ).order_by('price')}
