# Generated by Django 4.0.4 on 2022-05-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_feature_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='region',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
