# Generated by Django 4.2.5 on 2023-09-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cats_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='cats',
            name='text_cat',
            field=models.TextField(blank=True, null=True),
        ),
    ]
