# Generated by Django 4.2.6 on 2023-10-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_remove_comment_post'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='comment.comment'),
        ),
    ]
