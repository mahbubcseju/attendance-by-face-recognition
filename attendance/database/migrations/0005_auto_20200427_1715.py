# Generated by Django 3.0.4 on 2020-04-27 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20200427_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='user',
            new_name='supervisor',
        ),
    ]
