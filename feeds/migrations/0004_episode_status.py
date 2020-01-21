# Generated by Django 2.2.9 on 2020-01-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20200117_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='status',
            field=models.CharField(choices=[('unplayed', 'Unplayed'), ('ongoing', 'Ongoing'), ('finished', 'Finished')], default='unplayed', max_length=20),
        ),
    ]