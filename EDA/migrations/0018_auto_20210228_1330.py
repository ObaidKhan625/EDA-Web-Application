# Generated by Django 3.1.4 on 2021-02-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0017_auto_20210228_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scatterplotmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='scatterplotmodel',
            name='name',
            field=models.CharField(default='Bar Plot', max_length=200, primary_key=True, serialize=False),
        ),
    ]
