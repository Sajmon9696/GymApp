# Generated by Django 4.2.7 on 2023-12-14 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_programs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='link_do_youtube',
            new_name='link_to_youtube',
        ),
    ]