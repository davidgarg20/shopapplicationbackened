# Generated by Django 3.0.3 on 2020-03-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemimage',
            field=models.ImageField(null=True, upload_to='itemimages/'),
        ),
    ]
