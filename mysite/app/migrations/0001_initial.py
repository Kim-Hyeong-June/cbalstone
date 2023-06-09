# Generated by Django 4.2 on 2023-05-04 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.CharField(blank=True, max_length=255)),
                ('salary', models.CharField(blank=True, max_length=255)),
                ('contents', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='post_images')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('career', models.CharField(blank=True, max_length=255)),
                ('salary', models.CharField(blank=True, max_length=255)),
                ('company', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('start_at', models.CharField(blank=True, max_length=255)),
                ('end_at', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
