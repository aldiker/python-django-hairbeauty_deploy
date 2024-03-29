# Generated by Django 4.1.3 on 2022-11-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text_1', models.CharField(max_length=50)),
                ('text_2', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='carousel_img/%Y/%m/%d/')),
            ],
        ),
    ]
