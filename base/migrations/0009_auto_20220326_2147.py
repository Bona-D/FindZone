# Generated by Django 3.2.12 on 2022-03-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20220326_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='complete',
        ),
        migrations.AddField(
            model_name='room',
            name='complete',
            field=models.BooleanField(default=True),
        ),
    ]
