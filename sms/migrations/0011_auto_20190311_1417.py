# Generated by Django 2.1.7 on 2019-03-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0010_auto_20190311_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Look',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
