# Generated by Django 3.2.8 on 2021-10-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_network_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rezult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=25)),
                ('object_type', models.CharField(max_length=25)),
                ('rezult', models.BooleanField()),
            ],
        ),
    ]