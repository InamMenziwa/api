# Generated by Django 5.0.3 on 2024-06-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('cast', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('date_added', models.CharField(max_length=200)),
                ('release_year', models.IntegerField(max_length=200)),
                ('rating', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('listed_in', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
