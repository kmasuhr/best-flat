# Generated by Django 4.0.1 on 2022-01-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_flatoffer_ignore'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatoffer',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]