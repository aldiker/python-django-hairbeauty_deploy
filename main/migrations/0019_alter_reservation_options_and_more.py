# Generated by Django 4.1.3 on 2023-01-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_reservation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['-created_at'], 'verbose_name': 'Предварительная бронь', 'verbose_name_plural': 'Предварительные брони'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number_of_reservation',
            field=models.IntegerField(default=0, verbose_name='Номер брони'),
        ),
    ]