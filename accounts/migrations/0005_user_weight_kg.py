# Generated by Django 4.2.7 on 2023-12-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_bench_press_record_kg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='weight_kg',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]