import pytest
from accounts.models import Gender, User, Trainer
from django.db.utils import IntegrityError
from fixtures import user, trainer, gender
from training_programs.models import TrainingPlan




@pytest.mark.django_db
def test_gender_creation(gender):
    assert str(gender) == 'Male'


@pytest.mark.django_db
def test_user_creation(user):
    assert user.username == 'user1'
    assert user.gender.gender == 'Male'


@pytest.mark.django_db
def test_trainer_creation(trainer):
    assert trainer.user.username == 'user2'
    assert trainer.number_of_plans_made == 0


@pytest.mark.django_db
def test_user_creation_with_invalid_gender():
    with pytest.raises(ValueError):
        User.objects.create_user(username='user2', email='user2@example.com', password='password',
                                 gender='InvalidGender')


@pytest.mark.django_db
def test_trainer_creation_without_user():
    with pytest.raises(IntegrityError):
        Trainer.objects.create()


@pytest.mark.django_db
def test_add_people_to_ppl_on_training_with_new_training_plan(trainer, user):
    assert trainer.number_of_training_ppl == 0  # Upewnij się, że początkowo nie ma żadnych osób trenujących
    assert trainer.ppl_on_training.count() == 0

    # Tworzenie nowego planu treningowego
    TrainingPlan.objects.create(name='testname', description='testdesc', amount_of_days=3, trainer=trainer,
                                plan_owner=user, duration_in_weeks=4)

    trainer.refresh_from_db()

    assert trainer.number_of_training_ppl == 1  # Sprawdź, czy liczba osób trenujących zwiększyła się po utworzeniu nowego planu
    assert trainer.ppl_on_training.count() == 1  # Sprawdź, czy użytkownik został dodany do listy ppl_on_training
