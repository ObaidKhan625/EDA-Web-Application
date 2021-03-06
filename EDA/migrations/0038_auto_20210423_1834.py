# Generated by Django 3.1.4 on 2021-04-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0037_auto_20210422_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barplotmodel',
            name='color',
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='x',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='y',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boxplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boxplotmodel',
            name='x',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boxplotmodel',
            name='y',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='countplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='countplotmodel',
            name='x',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='histogramplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='histogramplotmodel',
            name='x',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='size',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='style',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='x',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='y',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='size',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='style',
            field=models.CharField(blank=True, choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='x',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='y',
            field=models.CharField(choices=[('Survived', 'Survived'), ('Pclass', 'Pclass'), ('Name', 'Name'), ('Sex', 'Sex'), ('Age', 'Age'), ('SibSp', 'SibSp'), ('Parch', 'Parch'), ('Ticket', 'Ticket'), ('Fare', 'Fare'), ('Cabin', 'Cabin'), ('Embarked', 'Embarked')], max_length=200, null=True),
        ),
    ]
