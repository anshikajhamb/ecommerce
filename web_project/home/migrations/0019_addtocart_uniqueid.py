# Generated by Django 3.2.7 on 2021-11-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20211105_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='uniqueid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
