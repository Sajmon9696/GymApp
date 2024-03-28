import pytest

from accounts.models import Gender, User, Trainer
from training_programs.models import TypesOfExercises, Exercise, TrainingPlan


@pytest.fixture
def gender():
    return Gender.objects.create(gender='Male')


@pytest.fixture
def user(gender):
    return User.objects.create_user(username='user1', email='user1@example.com', password='password', gender=gender)


@pytest.fixture
def trainer(gender):
    trainer = User.objects.create_user(username='user2', email='user2@example.com', password='password', gender=gender,
                                       is_trainer=True)
    return Trainer.objects.create(user=trainer)


@pytest.fixture
def types_of_exercise():
    return TypesOfExercises.objects.create(name="Cardio")


@pytest.fixture
def exercise(types_of_exercise):
    return Exercise.objects.create(name="Push-up", types=types_of_exercise,
                                       description="Description of push-up exercise",
                                       link_to_youtube="https://www.youtube.com/watch?v=IODxDxX7oi4")
@pytest.fixture
def plan(trainer, user):
    return TrainingPlan.objects.create(
        name="Test Plan",
        description="Test Description",
        amount_of_days=5,
        trainer=trainer,
        plan_owner=user
    )