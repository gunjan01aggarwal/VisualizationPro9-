# Generated by Django 3.2.25 on 2024-12-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0013_auto_20241208_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='insight',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='source',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
