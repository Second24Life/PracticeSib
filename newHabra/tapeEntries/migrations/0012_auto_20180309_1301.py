# Generated by Django 2.0.2 on 2018-03-09 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapeEntries', '0011_auto_20180309_1301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-createdDate']},
        ),
    ]