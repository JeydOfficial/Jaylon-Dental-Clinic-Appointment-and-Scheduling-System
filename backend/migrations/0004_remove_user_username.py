# Generated by Django 4.2.15 on 2024-08-26 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
