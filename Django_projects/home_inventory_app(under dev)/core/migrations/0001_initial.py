# Generated by Django 4.0.5 on 2022-06-18 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='category name')),
            ],
        ),
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='supercatogory name')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='subcategory name')),
                ('type', models.CharField(max_length=50, verbose_name='type')),
                ('qty', models.PositiveIntegerField(verbose_name='quantity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='item name')),
                ('desc', models.CharField(max_length=255, verbose_name='item description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='item price')),
                ('upc', models.IntegerField(max_length=12, verbose_name='item upc')),
                ('record_date', models.DateTimeField(verbose_name='date item recorded')),
                ('sell_by_date', models.DateField(verbose_name='item sell by date')),
                ('expire_date', models.DateField(verbose_name='item expiration date')),
                ('ct', models.PositiveIntegerField(verbose_name='item count')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subcategory')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='supercategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.supercategory'),
        ),
    ]
