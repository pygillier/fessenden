# Generated by Django 2.2.9 on 2020-01-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20200103_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]