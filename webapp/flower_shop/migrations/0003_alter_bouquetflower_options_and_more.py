# Generated by Django 5.1.2 on 2024-10-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_shop', '0002_add_sample_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bouquetflower',
            options={'verbose_name': 'Связь цветок-букет', 'verbose_name_plural': 'Связь цветы-букет'},
        ),
        migrations.AlterField(
            model_name='bouquetflower',
            name='quantity',
            field=models.IntegerField(verbose_name=' '),
        ),
    ]
