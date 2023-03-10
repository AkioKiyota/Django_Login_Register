# Generated by Django 4.1.4 on 2022-12-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_user_profile_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='about',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='phone_num',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='picture_url',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
