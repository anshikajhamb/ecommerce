# Generated by Django 3.2.7 on 2021-11-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
