# Generated by Django 4.1.3 on 2022-12-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.CharField(max_length=100),
        ),
    ]
