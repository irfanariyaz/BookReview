# Generated by Django 4.2.3 on 2023-07-18 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
