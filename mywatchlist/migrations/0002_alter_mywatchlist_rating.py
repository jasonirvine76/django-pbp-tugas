# Generated by Django 4.1 on 2022-09-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='rating',
            field=models.CharField(blank=True, choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=10, null=True),
        ),
    ]