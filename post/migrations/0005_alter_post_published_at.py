# Generated by Django 4.2.6 on 2023-10-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_post_readed_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]