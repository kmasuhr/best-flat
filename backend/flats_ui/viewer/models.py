from django.db import models


class FlatOffer(models.Model):
    version = models.PositiveIntegerField(default=1)
    is_latest = models.BooleanField(default=True)

    ignore = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)

    provider = models.CharField(max_length=100)
    provider_id = models.CharField(max_length=100)

    title = models.TextField(blank=True, null=True)

    price = models.FloatField(blank=True, null=True)
    price_per_meter = models.FloatField(blank=True, null=True)

    living_area = models.FloatField(blank=True, null=True)
    number_of_rooms = models.IntegerField(blank=True, null=True)

    floor = models.IntegerField(blank=True, null=True)
    floor_in_total = models.IntegerField(blank=True, null=True)
    last_floor = models.BooleanField(blank=True, null=True)

    year = models.IntegerField(blank=True, null=True)
    location = models.CharField(blank=True, null=True, max_length=255)

    url = models.URLField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def update(self, **kwargs):
        changed = False
        changes = {}
        for key, value in kwargs.items():
            if key in ['id']:
                continue
            if value != getattr(self, key):
                changed = True
                changes[key] = value

        if not changed:
            return

        print('Create offer', self.provider_id)

        self.is_latest = False
        self.save()

        self.id = None
        self.version += 1
        self.is_latest = True
        self.save()

        for key, value in changes.items():
            setattr(self, key, value)

        self.save()

    def __str__(self):
        return self.title if self.title is not None else '---'
