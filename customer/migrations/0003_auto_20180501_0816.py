# Generated by Django 2.0.4 on 2018-05-01 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20180430_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='amount',
            new_name='balance',
        ),
    ]
