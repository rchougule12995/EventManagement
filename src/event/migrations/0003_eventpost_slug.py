# Generated by Django 2.2 on 2019-04-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_eventpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpost',
            name='slug',
            field=models.SlugField(default='hello-world'),
            preserve_default=False,
        ),
    ]