# Generated by Django 4.2.5 on 2024-03-26 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0007_bid_is_selected'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='current_bid',
            new_name='expected_bid',
        ),
        migrations.RemoveField(
            model_name='auction',
            name='quantity',
        ),
    ]
