# Generated by Django 2.1.3 on 2019-01-12 19:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0012_auto_20190111_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfilio',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 12, 19, 34, 51, 238387, tzinfo=utc)),
        ),
    ]
