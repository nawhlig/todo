# Generated by Django 3.1.1 on 2020-09-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20200911_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]