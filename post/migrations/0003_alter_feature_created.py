# Generated by Django 3.2.6 on 2021-09-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210907_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
