# Generated by Django 2.2.12 on 2020-05-04 14:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
