# Generated by Django 3.2.7 on 2021-11-11 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer'),
        ),
    ]