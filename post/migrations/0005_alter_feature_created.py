# Generated by Django 4.0.4 on 2022-05-18 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_rename_content_feature_experience_feature_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
