# Generated by Django 3.0.6 on 2020-06-11 09:00

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exampleapp', '0005_auto_20200529_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='backlinks',
            field=jsonfield.fields.JSONField(blank=True, default='{}', verbose_name='backlinks'),
        ),
    ]