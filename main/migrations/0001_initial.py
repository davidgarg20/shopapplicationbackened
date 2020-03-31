# Generated by Django 3.0.3 on 2020-03-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.IntegerField()),
                ('itemname', models.CharField(max_length=100)),
                ('maxprice', models.IntegerField()),
                ('sellprice', models.IntegerField()),
                ('itemdetail', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('orderamount', models.CharField(max_length=100)),
                ('orderdate', models.CharField(max_length=100)),
                ('delstatus', models.CharField(max_length=100, null=True)),
                ('deltime', models.CharField(max_length=100, null=True)),
                ('deladdress', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='orderdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.IntegerField()),
                ('itemid', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('mobileno', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
    ]