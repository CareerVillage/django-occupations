# Generated by Django 3.0.7 on 2020-06-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_occupations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socbroadoccupation',
            name='soc_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='socdetailedoccupation',
            name='soc_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='socmajorgroup',
            name='soc_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='socminorgroup',
            name='soc_code',
            field=models.IntegerField(null=True),
        ),
    ]
