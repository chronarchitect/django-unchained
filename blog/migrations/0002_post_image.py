# Generated by Django 2.2.1 on 2019-05-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default='static/img/default-post-img.jpg', upload_to='uploads/%Y/%m/%d'),
        ),
    ]
