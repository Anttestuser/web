# Generated by Django 4.2.7 on 2023-12-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hey', '0002_uploadfiles_name_alter_uploadfiles_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file',
            field=models.ImageField(upload_to='images'),
        ),
    ]
