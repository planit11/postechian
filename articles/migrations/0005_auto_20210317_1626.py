# Generated by Django 3.1.7 on 2021-03-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210317_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumnail',
            field=models.ImageField(null=True, upload_to='article_img'),
        ),
    ]