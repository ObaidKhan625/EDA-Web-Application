# Generated by Django 3.1.4 on 2021-03-03 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0024_auto_20210303_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='histogramplotmodel',
            name='y',
        ),
    ]
