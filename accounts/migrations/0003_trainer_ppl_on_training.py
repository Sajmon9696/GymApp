# Generated by Django 4.2.7 on 2023-12-06 12:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_trainer_number_of_training_ppl'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='ppl_on_training',
            field=models.ManyToManyField(related_name='primary_key', to=settings.AUTH_USER_MODEL),
        ),
    ]
