# Generated by Django 3.2.25 on 2024-12-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0012_auto_20241208_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='added',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]