# Generated by Django 2.1 on 2019-03-14 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api', models.FloatField()),
                ('totalPercentage', models.FloatField()),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Tool')),
            ],
        ),
        migrations.CreateModel(
            name='Findability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_down', models.FloatField()),
                ('doi', models.FloatField()),
                ('description', models.FloatField()),
                ('versions', models.FloatField()),
                ('totalPercentage', models.FloatField()),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Tool')),
            ],
        ),
        migrations.CreateModel(
            name='Interoperability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compatibility', models.FloatField()),
                ('totalPercentage', models.FloatField()),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Tool')),
            ],
        ),
        migrations.CreateModel(
            name='Reusability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_repo', models.FloatField()),
                ('ontology', models.FloatField()),
                ('documentation', models.FloatField()),
                ('contact', models.FloatField()),
                ('citation', models.FloatField()),
                ('totalPercentage', models.FloatField()),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Tool')),
            ],
        ),
        migrations.RemoveField(
            model_name='fairscore',
            name='tool',
        ),
        migrations.DeleteModel(
            name='FairScore',
        ),
    ]
