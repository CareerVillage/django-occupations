# Generated by Django 3.0.7 on 2021-02-10 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_occupations', '0006_make_alttitle_to_occupation_m2m_part2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onetalternatetitle',
            name='soc_occupation',
        ),
    ]
