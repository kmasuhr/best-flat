# Generated by Django 4.0.1 on 2022-01-22 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_flatoffer_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatoffer',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
