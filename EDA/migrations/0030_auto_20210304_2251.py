# Generated by Django 3.1.4 on 2021-03-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0029_auto_20210304_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxplotmodel',
            name='fliersize',
            field=models.FloatField(default=5),
        ),
    ]
