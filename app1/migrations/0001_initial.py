# Generated by Django 5.0.3 on 2024-04-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('photo', models.FileField(blank=True, null=True, upload_to='user_pic/')),
                ('datetime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
