# Generated by Django 3.2.25 on 2024-12-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_alter_data_start_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='impact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
