# Generated by Django 3.2.25 on 2024-12-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_auto_20241208_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='end_year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]