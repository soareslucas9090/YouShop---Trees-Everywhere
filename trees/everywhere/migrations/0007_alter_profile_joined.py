# Generated by Django 5.0.6 on 2024-06-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everywhere', '0006_alter_profile_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joined',
            field=models.DateTimeField(null=True),
        ),
    ]