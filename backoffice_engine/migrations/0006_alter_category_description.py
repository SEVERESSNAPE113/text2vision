# Generated by Django 5.2.1 on 2025-06-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice_engine', '0005_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
