# Generated by Django 4.2.5 on 2023-09-12 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='percent',
            field=models.IntegerField(null=True),
        ),
    ]
