# Generated by Django 2.0.2 on 2018-03-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapeEntries', '0004_auto_20180305_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
