# Generated by Django 3.2.3 on 2022-12-02 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_profile_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='vegeterian',
            new_name='vegetarian',
        ),
    ]