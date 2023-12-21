# Generated by Django 4.2.8 on 2023-12-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0003_alter_advert_payment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='payment_options',
            field=models.CharField(choices=[('CASH', 'Cash only'), ('PAYPAL', 'PayPal only'), ('EITHER', 'Cash or Paypal')], default='EITHER', max_length=20),
        ),
        migrations.AlterField(
            model_name='advert',
            name='shippment_options',
            field=models.CharField(choices=[('COLLECTION', 'Collection Only'), ('POSTAGE', 'Royal Mail Only'), ('EITHER', 'Collection or Royal Mail delivery')], default='EITHER', max_length=50),
        ),
    ]