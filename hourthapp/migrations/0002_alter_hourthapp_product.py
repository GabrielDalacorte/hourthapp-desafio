# Generated by Django 3.2.7 on 2022-05-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hourthapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourthapp',
            name='product',
            field=models.FileField(upload_to='', verbose_name='products/'),
        ),
    ]