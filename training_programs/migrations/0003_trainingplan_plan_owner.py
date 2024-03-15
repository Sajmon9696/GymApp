# Generated by Django 4.2.7 on 2023-12-15 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training_programs', '0002_rename_link_do_youtube_exercise_link_to_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingplan',
            name='plan_owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]