# Generated by Django 3.1.7 on 2021-03-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210317_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='display_date',
            field=models.DateField(null=True),
        ),
    ]
