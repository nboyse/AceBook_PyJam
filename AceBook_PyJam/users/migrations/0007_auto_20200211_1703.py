# Generated by Django 3.0.3 on 2020-02-11 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_friend_current_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='user',
            new_name='users',
        ),
    ]
