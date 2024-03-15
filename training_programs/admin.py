from django.contrib import admin
from .models import Exercise, TypesOfExercises, Goal, TrainingPlanInfo, TrainingPlan, TrainingDay, ExerciseInPlan

# Register your models here.

admin.site.register(Exercise)
admin.site.register(TypesOfExercises)
admin.site.register(Goal)
admin.site.register(TrainingPlanInfo)
admin.site.register(TrainingPlan)
admin.site.register(TrainingDay)
admin.site.register(ExerciseInPlan)