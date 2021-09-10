# Generated by Django 3.1.4 on 2021-03-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0021_auto_20210301_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barplotmodel',
            name='capsize',
            field=models.FloatField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='errcolor',
            field=models.CharField(default='0.26', max_length=200),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='errwidth',
            field=models.FloatField(default=3, max_length=200),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='saturation',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='countplotmodel',
            name='dodge',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='countplotmodel',
            name='saturation',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='n_boot',
            field=models.IntegerField(default=1000),
        ),
    ]