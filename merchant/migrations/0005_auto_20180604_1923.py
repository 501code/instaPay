# Generated by Django 2.0.6 on 2018-06-04 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0004_payment_remote_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='spaceship',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='spaceship',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
