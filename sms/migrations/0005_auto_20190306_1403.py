# Generated by Django 2.1.7 on 2019-03-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_auto_20190306_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoing',
            name='access_code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='outgoing',
            name='service_id',
            field=models.CharField(max_length=50),
        ),
    ]