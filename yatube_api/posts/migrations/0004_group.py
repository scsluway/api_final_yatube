# Generated by Django 3.2.16 on 2024-06-18 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
