# Generated by Django 3.0.8 on 2020-07-30 10:24

from django.db import migrations, models
import enums


class Migration(migrations.Migration):

    dependencies = [
        ('hkCbbcApi', '0006_bullbearratioschema_close_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bullbearratioschema',
            name='source',
            field=models.IntegerField(choices=[(enums.CbbcDataSourceEnum['hkex'], 0), (enums.CbbcDataSourceEnum['credit_suisse'], 1)], default=0),
        ),
    ]