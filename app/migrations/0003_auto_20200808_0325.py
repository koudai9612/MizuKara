# Generated by Django 2.1.2 on 2020-08-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200808_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='sample_1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_10',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_5',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_6',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_8',
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_3',
            field=models.IntegerField(blank=True, null=True, verbose_name='量'),
        ),
    ]
