# Generated by Django 2.1 on 2019-03-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20190314_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='fairscore',
            name='reusability',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
