# Generated by Django 4.1.3 on 2022-11-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_navbar_options_navbar_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_me_enable', models.BooleanField()),
                ('contact_me', models.CharField(default='Связаться', max_length=50)),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=13, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254)),
                ('follow_us_enable', models.BooleanField()),
                ('follow_us', models.CharField(default='Подписаться', max_length=50)),
                ('twitter_url', models.CharField(max_length=100, verbose_name='Twitter')),
                ('facebook_url', models.CharField(max_length=100, verbose_name='Facebook')),
                ('linkedin_url', models.CharField(max_length=100, verbose_name='Linkedin')),
                ('instagram_url', models.CharField(max_length=100, verbose_name='Instagram')),
                ('open_hours_enable', models.BooleanField()),
                ('open_hours', models.CharField(default='Посетить', max_length=50)),
                ('days_period1', models.CharField(default='Понедельник - Пятница', max_length=50)),
                ('days_period2', models.CharField(default='Суббота', max_length=50)),
                ('days_period3', models.CharField(default='Воскресенье', max_length=50)),
                ('hours_period1', models.CharField(default='10:00 - 18:00', max_length=20)),
                ('hours_period2', models.CharField(default='10:00 - 14:00', max_length=20)),
                ('hours_period3', models.CharField(default='Выходной', max_length=20)),
                ('newsletters_enable', models.BooleanField()),
                ('newsletters', models.CharField(default='Быть в теме', max_length=50)),
            ],
        ),
    ]
