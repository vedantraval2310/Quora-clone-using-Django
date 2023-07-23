# Generated by Django 3.0.6 on 2020-07-04 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_notification_is_following_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='is_following_user',
            new_name='is_following_user_answers',
        ),
        migrations.AddField(
            model_name='notification',
            name='is_following_user_questions',
            field=models.BooleanField(default=False),
        ),
    ]
