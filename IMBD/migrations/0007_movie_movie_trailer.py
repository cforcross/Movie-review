# Generated by Django 3.0.4 on 2020-04-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMBD', '0006_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
