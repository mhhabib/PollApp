# Generated by Django 3.1.2 on 2020-11-08 12:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
