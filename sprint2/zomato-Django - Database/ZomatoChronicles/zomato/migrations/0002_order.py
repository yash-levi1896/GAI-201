# Generated by Django 3.2.20 on 2023-08-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('dishes', models.JSONField()),
                ('status', models.CharField(choices=[('preparing', 'Preparing'), ('received', 'Received'), ('ready for pickup', 'Ready For Pickup'), ('delivered', 'Delivered')], max_length=20)),
            ],
        ),
    ]
