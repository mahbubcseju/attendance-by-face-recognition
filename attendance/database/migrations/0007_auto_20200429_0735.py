# Generated by Django 3.0.4 on 2020-04-29 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_attendanceentry_attendanceperiod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendanceperiod',
            name='end_at',
        ),
        migrations.AddField(
            model_name='attendanceperiod',
            name='period',
            field=models.IntegerField(default=45, verbose_name='Period'),
        ),
    ]
