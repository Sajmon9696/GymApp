# Generated by Django 4.2.7 on 2024-01-23 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_gender_alter_user_gender_delete_gender2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='number_of_plans_made',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='number_of_training_ppl',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='ppl_on_training',
            field=models.ManyToManyField(blank=True, related_name='primary_key', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='bench_press_record_kg',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='dead_lift_record_kg',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='dips_record_amount',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='height_cm',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pull_up_record_amount',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='squat_record_kg',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight_kg',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]