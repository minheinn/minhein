# Generated by Django 4.2.2 on 2023-09-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
