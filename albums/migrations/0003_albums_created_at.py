# Generated by Django 3.2.9 on 2021-11-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_remove_albums_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
