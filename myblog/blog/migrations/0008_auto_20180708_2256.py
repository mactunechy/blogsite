# Generated by Django 2.2 on 2018-07-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180708_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
