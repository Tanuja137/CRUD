# Generated by Django 4.2.7 on 2024-02-14 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restro', '0002_alter_foodorder_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]