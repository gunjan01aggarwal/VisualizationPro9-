# Generated by Django 3.2.25 on 2024-12-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_alter_data_end_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='start_year',
            field=models.CharField(max_length=50),
        ),
    ]
