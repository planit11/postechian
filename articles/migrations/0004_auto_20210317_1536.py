# Generated by Django 3.1.7 on 2021-03-17 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210317_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumnail',
            field=models.ImageField(height_field=100, null=True, upload_to='article_img', width_field=100),
        ),
    ]
