# Generated by Django 2.2.4 on 2019-09-09 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laudosMedvet', '0005_auto_20190909_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animalmodel',
            old_name='estado',
            new_name='id_estado',
        ),
    ]
