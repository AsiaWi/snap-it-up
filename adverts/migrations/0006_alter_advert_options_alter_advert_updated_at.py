# Generated by Django 4.2.8 on 2023-12-13 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0005_rename_advert_owner_advert_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'ordering': ['-created_at', '-updated_at']},
        ),
        migrations.AlterField(
            model_name='advert',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]