import pytest
from django.db import IntegrityError
from training_programs.models import TypesOfExercises, Exercise
from fixtures import types_of_exercise, exercise


@pytest.mark.django_db
def test_create_types_of_exercises(types_of_exercise):
    assert types_of_exercise.name == "Cardio"


@pytest.mark.django_db
def test_create_exercise_with_types(types_of_exercise, exercise):
    assert exercise.name == "Push-up"
    assert exercise.description == "Description of push-up exercise"
    assert exercise.link_to_youtube == "https://www.youtube.com/watch?v=IODxDxX7oi4"
    assert exercise.types == types_of_exercise


@pytest.mark.django_db
def test_create_exercise_without_types():
    with pytest.raises(IntegrityError):
        Exercise.objects.create(name="Squat", description="Description of squat exercise",
                                link_to_youtube="https://www.youtube.com/watch?v=QKKZ9AGYTi4")
