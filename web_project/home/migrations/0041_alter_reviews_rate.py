# Generated by Django 3.2.7 on 2021-11-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_alter_reviews_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
