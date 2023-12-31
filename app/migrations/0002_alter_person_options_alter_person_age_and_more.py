# Generated by Django 4.2.6 on 2023-12-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Человека', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=1, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthDay',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.BooleanField(verbose_name='Гендер'),
        ),
    ]
