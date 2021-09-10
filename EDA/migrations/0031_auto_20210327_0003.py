# Generated by Django 3.1.7 on 2021-03-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0030_auto_20210304_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='x',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='y',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boxplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boxplotmodel',
            name='x',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boxplotmodel',
            name='y',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='countplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='countplotmodel',
            name='x',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='histogramplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='histogramplotmodel',
            name='x',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='size',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='style',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='x',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lineplotmodel',
            name='y',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='hue',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='size',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='style',
            field=models.CharField(blank=True, choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='x',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scatterplotmodel',
            name='y',
            field=models.CharField(choices=[('CUST_ID', 'CUST_ID'), ('BALANCE', 'BALANCE'), ('BALANCE_FREQUENCY', 'BALANCE_FREQUENCY'), ('PURCHASES', 'PURCHASES'), ('ONEOFF_PURCHASES', 'ONEOFF_PURCHASES'), ('INSTALLMENTS_PURCHASES', 'INSTALLMENTS_PURCHASES'), ('CASH_ADVANCE', 'CASH_ADVANCE'), ('PURCHASES_FREQUENCY', 'PURCHASES_FREQUENCY'), ('ONEOFF_PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'), ('PURCHASES_INSTALLMENTS_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'), ('CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'), ('CASH_ADVANCE_TRX', 'CASH_ADVANCE_TRX'), ('PURCHASES_TRX', 'PURCHASES_TRX'), ('CREDIT_LIMIT', 'CREDIT_LIMIT'), ('PAYMENTS', 'PAYMENTS'), ('MINIMUM_PAYMENTS', 'MINIMUM_PAYMENTS'), ('PRC_FULL_PAYMENT', 'PRC_FULL_PAYMENT'), ('TENURE', 'TENURE')], max_length=200, null=True),
        ),
    ]
