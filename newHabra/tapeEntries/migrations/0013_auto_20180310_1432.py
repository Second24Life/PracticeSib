# Generated by Django 2.0.2 on 2018-03-10 14:32

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tapeEntries', '0012_auto_20180309_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
