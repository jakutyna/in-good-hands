# Generated by Django 2.2.10 on 2020-11-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_donation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='categories',
            field=models.ManyToManyField(blank=True, to='charity_donation.Category'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='categories',
            field=models.ManyToManyField(blank=True, to='charity_donation.Category'),
        ),
    ]
