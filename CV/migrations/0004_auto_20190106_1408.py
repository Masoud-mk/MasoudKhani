# Generated by Django 2.1.3 on 2019-01-06 14:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0003_auto_20190106_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 6, 14, 8, 8, 415146, tzinfo=utc)),
        ),
    ]
