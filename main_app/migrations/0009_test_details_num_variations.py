# Generated by Django 2.0.2 on 2018-03-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_variation_varid'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_details',
            name='num_variations',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
