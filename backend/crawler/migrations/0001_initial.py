# Generated by Django 5.1.6 on 2025-02-28 14:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_url', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('product_link', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
