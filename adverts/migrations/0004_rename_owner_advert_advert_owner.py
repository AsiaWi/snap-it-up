# Generated by Django 4.2.8 on 2023-12-13 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0003_rename_advert_owner_advert_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='owner',
            new_name='advert_owner',
        ),
    ]