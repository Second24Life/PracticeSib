# Generated by Django 2.0.2 on 2018-03-09 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapeEntries', '0008_auto_20180309_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
