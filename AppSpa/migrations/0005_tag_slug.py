# Generated by Django 3.2.9 on 2021-12-01 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSpa', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
