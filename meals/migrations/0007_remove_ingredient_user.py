# Generated by Django 3.2 on 2022-04-10 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0006_auto_20220410_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='user',
        ),
    ]
