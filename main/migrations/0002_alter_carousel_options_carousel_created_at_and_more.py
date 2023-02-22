# Generated by Django 4.1.3 on 2022-11-18 14:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['-created_at'], 'verbose_name': 'Карусель', 'verbose_name_plural': 'Карусели'},
        ),
        migrations.AddField(
            model_name='carousel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создан'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carousel',
            name='photo',
            field=models.ImageField(upload_to='carousel_img/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='text_1',
            field=models.CharField(max_length=50, verbose_name='Текст 1'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='text_2',
            field=models.CharField(max_length=50, verbose_name='Текст 2'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
