# Generated by Django 3.1.4 on 2021-03-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0025_remove_histogramplotmodel_y'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histogramplotmodel',
            name='element',
            field=models.CharField(choices=[('bars', 'bars'), ('step', 'step'), ('poly', 'poly')], default='bars', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='histogramplotmodel',
            name='fill',
            field=models.CharField(choices=[('True', True), ('False', False)], default=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='histogramplotmodel',
            name='multiple',
            field=models.CharField(choices=[('layer', 'layer'), ('dodge', 'dodge'), ('stack', 'stack'), ('fill', 'fill')], default='layer', max_length=200, null=True),
        ),
    ]
