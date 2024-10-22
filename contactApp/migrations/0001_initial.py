# Generated by Django 4.2.1 on 2023-05-24 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='招聘岗位')),
                ('description', models.TextField(verbose_name='岗位要求')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '招聘广告',
                'verbose_name_plural': '招聘广告',
                'ordering': ('-publishDate',),
            },
        ),
    ]
