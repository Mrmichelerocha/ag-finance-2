# Generated by Django 4.2.4 on 2023-11-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyse',
            name='maximum',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='minimum',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='price_now',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='buy',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sell',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
