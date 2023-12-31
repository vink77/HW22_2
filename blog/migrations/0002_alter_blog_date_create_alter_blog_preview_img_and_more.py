# Generated by Django 4.2.5 on 2023-09-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_create',
            field=models.DateField(default='2023-09-19', verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='preview_img',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images/', verbose_name='Превью(изображение)'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='просмотры'),
        ),
    ]
