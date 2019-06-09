# Generated by Django 2.1.5 on 2019-01-09 00:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ciss_exhi', '0005_auto_20190109_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='port_date_last',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last update'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='stra_date_last',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last update'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='stra_date_pub',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published'),
        ),
    ]
