# Generated by Django 3.2 on 2023-02-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postnews',
            name='image',
            field=models.ImageField(blank=True, unique=True, upload_to=''),
        ),
    ]
