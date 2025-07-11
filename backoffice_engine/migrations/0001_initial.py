# Generated by Django 5.2.1 on 2025-06-13 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('duration_days', models.IntegerField()),
                ('credit', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'plan',
            },
        ),
        migrations.CreateModel(
            name='Suggested_prompt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prompt', models.TextField()),
            ],
            options={
                'db_table': 'sugested_prompt',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=13, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('otp_used', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(default='active', max_length=20)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice_engine.plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice_engine.user')),
            ],
            options={
                'db_table': 'subscription',
            },
        ),
        migrations.CreateModel(
            name='Generated_image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('system_prompt', models.TextField()),
                ('user_prompt', models.TextField()),
                ('image', models.FileField(upload_to='')),
                ('temprature', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice_engine.user')),
            ],
            options={
                'db_table': 'generated_image',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice_engine.user')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
