# Generated by Django 2.2.9 on 2020-01-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='last_fetched_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last fetch date'),
        ),
    ]
