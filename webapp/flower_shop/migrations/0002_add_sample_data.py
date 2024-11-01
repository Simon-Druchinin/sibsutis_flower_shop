# Добавить некоторые образцы цветов
from django.db import migrations
from flower_shop.models import *


def add_sample_data(apps, schema_editor):   
    flowers = [
        Flower(name='Роза', description='Классическая красная роза', price=10.99),
        Flower(name='Тюльпан', description='Яркий желтый тюльпан', price=8.99),
        Flower(name='Маргаритка', description='Веселая белая маргаритка', price=6.99),
    ]
    Flower.objects.bulk_create(flowers)

    # Добавить некоторые образцы букетов
    bouquets = [
        Bouquet(name='Романтика', description='Букет красных роз', price=49.99),
        Bouquet(name='Солнечный свет', description='Букет желтых тюльпанов', price=39.99),
        Bouquet(name='Садовая вечеринка', description='Букет смешанных цветов', price=29.99),
    ]
    Bouquet.objects.bulk_create(bouquets)

    bouquet_flowers = [
        BouquetFlower(bouquet=bouquets[0], flower=flowers[0], quantity=3),
        BouquetFlower(bouquet=bouquets[0], flower=flowers[1], quantity=2),
        BouquetFlower(bouquet=bouquets[1], flower=flowers[1], quantity=5),
        BouquetFlower(bouquet=bouquets[2], flower=flowers[0], quantity=2),
        BouquetFlower(bouquet=bouquets[2], flower=flowers[2], quantity=3),
    ]
    BouquetFlower.objects.bulk_create(bouquet_flowers)

class Migration(migrations.Migration):
    dependencies = [
        ('flower_shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_data),
    ]