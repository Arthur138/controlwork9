# Generated by Django 4.1.6 on 2023-02-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, max_length=13, null=True, verbose_name='Телефон'),
        ),
    ]
