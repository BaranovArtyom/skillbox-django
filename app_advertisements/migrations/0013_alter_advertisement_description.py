# Generated by Django 3.2.5 on 2021-07-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0012_rubric_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(default='', max_length=1000, verbose_name='Описание'),
        ),
    ]
