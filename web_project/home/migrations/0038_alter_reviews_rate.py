# Generated by Django 3.2.7 on 2021-11-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_alter_reviews_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
