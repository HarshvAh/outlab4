# Generated by Django 3.2.7 on 2021-09-19 05:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_auto_20210919_1011'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
    ]