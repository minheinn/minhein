# Generated by Django 4.2.2 on 2023-09-06 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_about_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='birth_day',
            new_name='birthday',
        ),
    ]