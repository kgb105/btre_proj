# Generated by Django 3.0.5 on 2020-04-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]