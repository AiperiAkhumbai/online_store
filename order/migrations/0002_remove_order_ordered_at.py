# Generated by Django 3.1.3 on 2020-12-01 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_at',
        ),
    ]