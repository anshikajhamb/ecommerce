# Generated by Django 3.2.7 on 2021-11-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
