# Generated by Django 4.1.6 on 2023-02-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Телефон'),
        ),
    ]
