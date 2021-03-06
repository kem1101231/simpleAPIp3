# Generated by Django 3.1.6 on 2021-06-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20210602_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField()),
                ('batchnum', models.IntegerField()),
                ('unitprice', models.FloatField()),
                ('sellingprice', models.FloatField()),
                ('quantity', models.FloatField()),
                ('barcode', models.IntegerField()),
                ('inventory_code', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('uom', models.CharField(max_length=255, null=True)),
                ('barcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, null=True)),
                ('date', models.DateField()),
                ('supplier', models.CharField(max_length=255, null=True)),
                ('total_cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_parent', models.CharField(max_length=255, null=True)),
                ('product_code', models.CharField(max_length=255, null=True)),
                ('cost_per_unit', models.FloatField()),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=255, null=True)),
                ('ornumber', models.IntegerField()),
                ('totalSale', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_parent', models.CharField(max_length=255, null=True)),
                ('inven_id', models.CharField(max_length=255, null=True)),
                ('product_code', models.CharField(max_length=255, null=True)),
                ('price_per_unit', models.FloatField()),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('business_type', models.CharField(max_length=255, null=True)),
                ('code', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
