# Generated by Django 3.0.8 on 2020-09-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hkCbbcApi', '0009_auto_20200909_1311'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='bullbearratioschema',
            index=models.Index(fields=['trade_date'], name='bull_bear_r_trade_d_7bb550_idx'),
        ),
        migrations.AddIndex(
            model_name='stockschema',
            index=models.Index(fields=['stock_abbv'], name='stocks_stock_a_0f8948_idx'),
        ),
    ]
