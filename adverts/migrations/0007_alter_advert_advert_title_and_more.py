# Generated by Django 4.2.8 on 2023-12-16 19:50

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('adverts', '0006_alter_advert_options_alter_advert_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='advert_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='advert',
            name='payment_options',
            field=models.CharField(choices=[('cash', 'Cash only'), ('PayPal', 'PayPal only'), ('either', 'Cash or Paypal')], default='either', max_length=20),
        ),
        migrations.AlterField(
            model_name='advert',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
