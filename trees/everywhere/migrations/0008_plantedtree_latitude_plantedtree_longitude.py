# Generated by Django 5.0.6 on 2024-06-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everywhere', '0007_alter_profile_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantedtree',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plantedtree',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
