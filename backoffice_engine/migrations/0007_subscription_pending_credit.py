# Generated by Django 5.2.1 on 2025-06-18 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice_engine', '0006_alter_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='pending_credit',
            field=models.IntegerField(default=0),
        ),
    ]
