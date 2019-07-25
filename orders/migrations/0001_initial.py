# Generated by Django 2.2.3 on 2019-07-25 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketplace', models.CharField(max_length=100)),
                ('lengow', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_hour', models.DateTimeField(verbose_name='Date de la commande')),
                ('amount', models.CharField(max_length=100)),
                ('marketplace_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Marketplace')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Status')),
            ],
            options={
                'ordering': ['date_hour'],
            },
        ),
    ]