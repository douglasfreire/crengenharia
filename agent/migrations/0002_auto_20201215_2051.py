# Generated by Django 2.2.17 on 2020-12-15 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesrepresentative',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]