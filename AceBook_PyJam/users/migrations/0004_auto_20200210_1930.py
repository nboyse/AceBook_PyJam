# Generated by Django 2.2.10 on 2020-02-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_like',
            field=models.BooleanField(null=True),
        ),
    ]
