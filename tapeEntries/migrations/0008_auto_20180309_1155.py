# Generated by Django 2.0.2 on 2018-03-09 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tapeEntries', '0007_auto_20180306_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='post',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
