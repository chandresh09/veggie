# Generated by Django 4.2.3 on 2023-08-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegrecords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veg',
            name='color',
            field=models.CharField(max_length=50),
        ),
    ]
