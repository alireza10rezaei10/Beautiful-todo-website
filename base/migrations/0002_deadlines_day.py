# Generated by Django 3.2.3 on 2021-06-03 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deadlines',
            name='day',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
