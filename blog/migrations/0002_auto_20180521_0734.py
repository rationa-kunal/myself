# Generated by Django 2.0.5 on 2018-05-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='img_url',
            field=models.URLField(default='https://i.imgur.com/1OxsSsl.jpg'),
        ),
    ]
