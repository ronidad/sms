# Generated by Django 2.1.7 on 2019-03-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0008_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
