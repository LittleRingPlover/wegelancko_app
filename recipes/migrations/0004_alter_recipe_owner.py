# Generated by Django 4.1.3 on 2022-12-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='owner',
            field=models.CharField(max_length=200),
        ),
    ]
