from django.db import models
from accounts.models import Trainer, User


# Create your models here.

class Goal(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class TypesOfExercises(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    types = models.ForeignKey(TypesOfExercises, on_delete=models.CASCADE)
    description = models.TextField()
    link_to_youtube = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name


class TrainingPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount_of_days = models.PositiveIntegerField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    plan_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class TrainingDay(models.Model):
    plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()
    exercises = models.ManyToManyField(Exercise, through='ExerciseInPlan')

    def __str__(self):
        return f'Dzien - {self.day_number}'


class ExerciseInPlan(models.Model):
    training_day = models.ForeignKey(TrainingDay, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps_amount = models.PositiveIntegerField()
    sets_amount = models.PositiveIntegerField()
    pause = models.PositiveIntegerField()
    tempo = models.CharField(max_length=7)


class TrainingPlanInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goals = models.ManyToManyField(Goal)
    time_of_one_training_in_minutes = models.PositiveIntegerField(help_text="Czas treningu w minutach")
    amount_of_days = models.PositiveIntegerField(help_text="Liczba dni")
    prefer_exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f"Zapytanie urzytkownika {self.user}, o plan trenigowy"


