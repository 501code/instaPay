# Generated by Django 2.0.6 on 2018-06-02 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='spaceship',
            name='currency',
            field=models.CharField(default='KES', max_length=55),
        ),
        migrations.AddField(
            model_name='payment',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='merchant.SpaceShip'),
        ),
    ]
