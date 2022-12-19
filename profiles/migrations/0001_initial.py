# Generated by Django 4.1.4 on 2022-12-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_url', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=50)),
                ('phone_num', models.CharField(max_length=15)),
            ],
        ),
    ]