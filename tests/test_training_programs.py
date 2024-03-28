import pytest
from training_programs.models import TrainingPlan, TrainingDay, ExerciseInPlan, TrainingPlanInfo
from fixtures import user, trainer, gender, types_of_exercise, exercise, plan



@pytest.mark.django_db
def test_training_plan_creation(plan,trainer, user):
    assert plan.name == "Test Plan"
    assert plan.amount_of_days == 5
    assert plan.trainer == trainer
    assert plan.plan_owner == user

@pytest.mark.django_db
def test_training_day_creation(plan):
    # Create a training plan
    day = TrainingDay.objects.create(
        plan=plan,
        day_number=1
    )
    assert str(day) == "Dzien - 1"

@pytest.mark.django_db
def test_exercise_in_plan_creation(exercise, plan):

    # Create a training day
    day = TrainingDay.objects.create(
        plan=plan,
        day_number=1
    )
    exercise_in_plan = ExerciseInPlan.objects.create(
        training_day=day,
        exercise=exercise,
        reps_amount=10,
        sets_amount=3,
        pause=60,
        tempo="2111"
    )
    assert exercise_in_plan.reps_amount == 10
    assert exercise_in_plan.sets_amount == 3
    assert exercise_in_plan.pause == 60
    assert exercise_in_plan.tempo == "2111"

@pytest.mark.django_db
def test_training_plan_info_creation(user):
    plan_info = TrainingPlanInfo.objects.create(
        user=user,
        time_of_one_training_in_minutes=60,
        amount_of_days=5
    )
    assert plan_info.user == user
    assert plan_info.time_of_one_training_in_minutes == 60
    assert plan_info.amount_of_days == 5

@pytest.mark.django_db
def test_training_plan_save(trainer, user, plan):
    assert trainer.number_of_plans_made == 1
    assert trainer.number_of_training_ppl == 1