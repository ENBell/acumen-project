# Generated by Django 2.0.2 on 2018-03-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20180305_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='varid',
            field=models.IntegerField(default=0),
        ),
    ]
