# Generated by Django 3.2.8 on 2021-10-30 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='network',
            name='place',
        ),
    ]