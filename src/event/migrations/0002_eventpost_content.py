# Generated by Django 2.2 on 2019-04-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpost',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]