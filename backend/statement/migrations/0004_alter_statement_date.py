# Generated by Django 3.2.8 on 2021-10-30 21:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0003_alter_statement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 21, 41, 57, 44156, tzinfo=utc)),
        ),
    ]
