# Generated by Django 4.2.1 on 2023-05-25 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0002_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2023-05-25', max_length=20, verbose_name='出生日期'),
        ),
    ]
