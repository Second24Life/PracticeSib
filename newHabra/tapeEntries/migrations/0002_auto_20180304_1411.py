# Generated by Django 2.0.2 on 2018-03-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapeEntries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastLoginDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
