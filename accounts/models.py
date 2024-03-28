from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey, PositiveSmallIntegerField, Model, DO_NOTHING, CharField
from .validators import validate_alpha, validate_name_length

# Create your models here.

class Gender(Model):
    """
       Model reprezentujący płeć użytkownika.
       """
    gender = CharField(max_length=10)

    def __str__(self):
        return self.gender


class User(AbstractUser):
    """
        Rozszerzony model użytkownika reprezentujący użytkowników aplikacji.
        """
    is_trainer = models.BooleanField(default=False)
    gender = ForeignKey(Gender, on_delete=DO_NOTHING, null=True, blank=True)
    height_cm = PositiveSmallIntegerField(null=True, blank=True)
    weight_kg = PositiveSmallIntegerField(null=True, blank=True)
    squat_record_kg = PositiveSmallIntegerField(null=True, blank=True)
    dead_lift_record_kg = PositiveSmallIntegerField(null=True, blank=True)
    bench_press_record_kg = PositiveSmallIntegerField(null=True, blank=True)
    pull_up_record_amount = PositiveSmallIntegerField(null=True, blank=True)
    dips_record_amount = PositiveSmallIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=30, validators=[validate_alpha, validate_name_length])
    last_name = models.CharField(max_length=30, validators=[validate_alpha, validate_name_length])

    def __str__(self):
        return f'{self.username}'


class Trainer(Model):
    """
       Model reprezentujący trenera w aplikacji.
       """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True)
    ppl_on_training = models.ManyToManyField(User, related_name='primary_key', blank=True)
    number_of_training_ppl = PositiveSmallIntegerField(default=0, blank=True)
    number_of_plans_made = PositiveSmallIntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.user}'

    def increment_number_of_plans_made(self):
        self.number_of_plans_made += 1
        self.save(update_fields=['number_of_plans_made'])

    def increment_number_of_training_ppl(self):
        self.number_of_training_ppl += 1
        self.save(update_fields=['number_of_training_ppl'])


