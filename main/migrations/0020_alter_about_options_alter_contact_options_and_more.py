# Generated by Django 4.1.3 on 2023-01-17 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_reservation_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['pk'], 'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['pk'], 'verbose_name': 'Наши контакты', 'verbose_name_plural': 'Наши контакты'},
        ),
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ['-created_at'], 'verbose_name': 'Акция', 'verbose_name_plural': 'Акции'},
        ),
        migrations.AlterModelOptions(
            name='offerbooking',
            options={'ordering': ['pk'], 'verbose_name': 'Бронь по акции', 'verbose_name_plural': 'Брони по акции'},
        ),
    ]
