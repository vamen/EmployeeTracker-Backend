# Generated by Django 2.1.4 on 2019-02-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20190202_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracktable',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
