# Generated by Django 4.2.5 on 2024-03-27 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0010_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='spice',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapi.seller'),
        ),
    ]
