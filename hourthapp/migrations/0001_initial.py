# Generated by Django 3.2.7 on 2022-05-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HourthApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=150)),
                ('insertion_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
