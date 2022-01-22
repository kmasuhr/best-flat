import json

from django.core.management import BaseCommand
from flats_ui.viewer.models import FlatOffer


class Command(BaseCommand):
    help = 'Load ingredients from JSON file'

    def handle(self, *args, **options):
        file_path = '/Users/karol.masuhr/repos/best-flat/scrapy/flats/flats.json'
        # purge scrapy file
        # run scrapy

        f = open(file_path)
        data = json.load(f)

        for flat in data:
            provider_id = flat.get('id')
            if not FlatOffer.objects.filter(provider_id=provider_id).exists():
                FlatOffer.objects.create(
                    provider='TROJMIASTO',
                    provider_id=provider_id,

                    title=flat.get('title'),

                    price=flat.get('price'),
                    price_per_meter=flat.get('price_per_meter'),

                    living_area=flat.get('living_area'),
                    number_of_rooms=flat.get('number_of_rooms'),

                    floor=flat.get('floor'),
                    floor_in_total=flat.get('floor_in_total'),
                    last_floor=flat.get('last_floor'),

                    year=flat.get('year'),
                    location=flat.get('location'),

                    url=flat.get('url'),
                    thumbnail=flat.get('thumbnail'),
                )
            else:
                instance = FlatOffer.objects.get(provider_id=provider_id, is_latest=True)
                instance.update(**flat)
