# Generated by Django 3.0.3 on 2020-07-01 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20200630_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='add_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
