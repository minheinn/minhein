# Generated by Django 4.2.5 on 2023-09-07 07:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rename_birth_day_about_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
