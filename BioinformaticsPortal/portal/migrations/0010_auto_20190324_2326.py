# Generated by Django 2.1 on 2019-03-24 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20190324_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline',
            name='accessibility',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pipeline',
            name='findability',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pipeline',
            name='interoperability',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pipeline',
            name='reusability',
            field=models.FloatField(null=True),
        ),
    ]
