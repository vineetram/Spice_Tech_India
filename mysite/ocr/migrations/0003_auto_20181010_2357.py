# Generated by Django 2.1.2 on 2018-10-10 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0002_auto_20181010_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='image',
            new_name='docfile',
        ),
    ]