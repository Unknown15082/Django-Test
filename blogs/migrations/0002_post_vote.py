# Generated by Django 4.0.2 on 2022-02-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vote',
            field=models.IntegerField(default=0, verbose_name='Number of votes'),
        ),
    ]