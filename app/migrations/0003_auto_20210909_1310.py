# Generated by Django 3.2.7 on 2021-09-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210909_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='count_stars',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='version',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='version',
            name='price',
            field=models.IntegerField(),
        ),
    ]
