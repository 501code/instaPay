# Generated by Django 2.0.6 on 2018-06-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0005_auto_20180604_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spaceship',
            name='image',
            field=models.ImageField(default='spaceship.jpg', upload_to=''),
        ),
    ]
