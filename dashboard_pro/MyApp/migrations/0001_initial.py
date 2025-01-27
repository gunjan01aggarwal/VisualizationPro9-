# Generated by Django 3.2.25 on 2024-12-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.IntegerField()),
                ('intensity', models.IntegerField()),
                ('sector', models.CharField(max_length=300)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.TextField()),
                ('url', models.TextField()),
                ('region', models.CharField(max_length=200)),
                ('start_year', models.IntegerField()),
                ('impact', models.IntegerField()),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField()),
                ('country', models.CharField(max_length=200)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(max_length=200)),
                ('source', models.TextField()),
                ('title', models.TextField()),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
