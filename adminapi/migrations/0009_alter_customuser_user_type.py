# Generated by Django 4.2.5 on 2024-03-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0008_rename_current_bid_auction_expected_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Seller', 'Seller')], default='Seller', max_length=50),
        ),
    ]
