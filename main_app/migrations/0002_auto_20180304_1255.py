# Generated by Django 2.0.2 on 2018-03-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acubox',
            name='content_type',
            field=models.CharField(default='apples', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acubox',
            name='contents',
            field=models.CharField(default='bananas', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acubox',
            name='name',
            field=models.CharField(default='grapes', max_length=10000),
            preserve_default=False,
        ),
    ]
