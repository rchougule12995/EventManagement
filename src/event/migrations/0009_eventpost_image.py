# Generated by Django 2.2 on 2019-04-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20190403_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]