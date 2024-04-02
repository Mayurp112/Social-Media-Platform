# Generated by Django 4.2.7 on 2024-04-02 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/post_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/post_videos/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_pictures/'),
        ),
        migrations.CreateModel(
            name='PrivacySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_privacy', models.CharField(choices=[('public', 'Public'), ('friends', 'Friends'), ('private', 'Private')], default='public', max_length=20)),
                ('profile_privacy', models.CharField(choices=[('public', 'Public'), ('friends', 'Friends'), ('private', 'Private')], default='public', max_length=20)),
                ('followers_privacy', models.CharField(choices=[('public', 'Public'), ('friends', 'Friends'), ('private', 'Private')], default='public', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
