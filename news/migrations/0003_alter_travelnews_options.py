# Generated by Django 5.1.4 on 2024-12-11 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_travelnews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='travelnews',
            options={'ordering': ['-published_date']},
        ),
    ]
