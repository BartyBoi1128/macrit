# Generated by Django 3.2.3 on 2022-12-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.CharField(max_length=254, null=True),
        ),
    ]