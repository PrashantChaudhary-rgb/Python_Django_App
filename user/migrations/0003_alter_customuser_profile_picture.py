# Generated by Django 5.0.1 on 2024-01-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_profile_picture_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics/'),
        ),
    ]
