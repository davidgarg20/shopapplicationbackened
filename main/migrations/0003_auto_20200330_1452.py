# Generated by Django 3.0.3 on 2020-03-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_itemimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliveryaddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('orderno', models.IntegerField()),
                ('delname', models.CharField(max_length=100)),
                ('delstreet', models.CharField(max_length=100)),
                ('delvillage', models.CharField(max_length=100)),
                ('delcity', models.CharField(max_length=100)),
                ('delzip', models.IntegerField()),
                ('delphone', models.IntegerField()),
                ('delnote', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='deliverycharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverycharge', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='itemimage',
            field=models.ImageField(upload_to='itemimages/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='deladdress',
            field=models.CharField(max_length=100, null=True),
        ),
    ]