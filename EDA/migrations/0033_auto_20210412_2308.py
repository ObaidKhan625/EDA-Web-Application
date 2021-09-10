# Generated by Django 3.1.4 on 2021-04-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0032_auto_20210412_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='x',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='y',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boxplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boxplotmodel',
            name='x',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boxplotmodel',
            name='y',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='countplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='countplotmodel',
            name='x',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='histogramplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='histogramplotmodel',
            name='x',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='size',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='style',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='x',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='y',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='size',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='style',
            field=models.CharField(blank=True, choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='x',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='y',
            field=models.CharField(choices=[('anime_id', 'anime_id'), ('name', 'name'), ('genre', 'genre'), ('type', 'type'), ('episodes', 'episodes'), ('rating', 'rating'), ('members', 'members')], max_length=200, null=True),
        ),
    ]