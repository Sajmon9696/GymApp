from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView
from django import forms

from accounts.models import User
from .forms import TrainingPlanInfoForm, ExerciseInPlanForm, TrainingPlanForm, AddExerciseForm
from .models import TrainingPlan, TrainingDay, Exercise, TrainingPlanInfo


# Create your views here.
@login_required
def create_training_plan_info(request):
    """
        Widok tworzenia zapytania o plan treningowy.
        Sprawdza, czy istnieje już zapytanie o planie dla użytkownika.
        Przekierowuje użytkownika do widoku detali pytania dotyczącego planu, jeśli już istnieją informacje o planie dla
        tego użytkownika.
        W przeciwnym razie, po zatwierdzeniu poprawnego formularza, zapisuje informacje o planie i przekierowuje
        użytkownika do widoku detali pytania dotyczącego planu.
        """
    existing_plan_info = TrainingPlanInfo.objects.filter(user=request.user).first()
    if existing_plan_info:
        return redirect('training_programs:plan_question_detail', pk=existing_plan_info.id)
    if request.method == 'POST':
        form = TrainingPlanInfoForm(request.POST)

        if form.is_valid():
            training_form = form.save(commit=False)
            training_form.user = request.user
            training_form.save()
            training_form.goals.set(form.cleaned_data.get('goals'))
            training_form.prefer_exercises.set(form.cleaned_data.get('prefer_exercises'))
            existing_plan_info = TrainingPlanInfo.objects.filter(user=request.user).first()
            return redirect('training_programs:plan_question_detail', pk=existing_plan_info.id)
        return render(request, 'training_programs/training_plan_info_form.html', {'form': form})
    else:
        form = TrainingPlanInfoForm()
    return render(request, 'training_programs/training_plan_info_form.html', {'form': form})


@login_required
def create_training_plan(request):
    """
        Widok tworzenia planu treningowego.
        Po zatwierdzeniu formularza, zapisuje informacje o planie treningowym i
        przekierowuje użytkownika do strony głównej konta.
        """
    if request.method == 'POST':
        form = TrainingPlanForm(request.POST)
        plan_owner_id = request.session.get('plan_owner_id')
        plan_question_id = request.session.get('plan_question_id')
        print(plan_owner_id)
        if form.is_valid():
            training_program_form = form.save(commit=False)
            training_program_form.trainer = request.user.trainer
            training_program_form.save()
            TrainingPlanInfo.objects.filter(id=plan_question_id).delete()
            return redirect('accounts:main')
        return render(request, 'training_programs/create_training_plan.html', {'form': form})

    else:
        plan_owner_id = request.GET.get('plan_owner_id')
        plan_question_id = request.GET.get('plan_question_id')
        print(type(plan_question_id))
        if plan_owner_id:
            request.session['plan_owner_id'] = plan_owner_id
            request.session['plan_question_id'] = plan_question_id
            initial_data = {'plan_owner': plan_owner_id}
            form = TrainingPlanForm(initial=initial_data)
            form.fields['plan_owner'].widget = forms.HiddenInput()
        else:
            form = TrainingPlanForm()
    return render(request, 'training_programs/create_training_plan.html', {'form': form})


@receiver(post_save, sender=TrainingPlan)
def create_training_days(sender, instance, created, **kwargs):
    """
        Funkcja obsługująca sygnał po zapisaniu nowego obiektu TrainingPlan.
        Tworzy odpowiednią liczbę dni treningowych dla nowo utworzonego planu treningowego.
        """
    if created:
        for day_number in range(1, instance.amount_of_days + 1):
            TrainingDay.objects.create(plan=instance, day_number=day_number)


@login_required
def create_training_plan_day(request, training_plan_id):
    """
        Widok tworzenia dnia planu treningowego.
        Po zatwierdzeniu formularza, zapisuje nowy dzień treningowy przypisany do danego planu treningowego.
        """
    training_plan = TrainingPlan.objects.get(pk=training_plan_id)
    training_day = TrainingDay.objects.filter(plan=training_plan_id)

    print(training_day)
    if request.method == 'POST':
        form = ExerciseInPlanForm(request.POST)
        form.fields['training_day'].queryset = training_day
        if form.is_valid():
            exercise_in_plan = form.save(commit=False)
            exercise_in_plan.save()
            return redirect('training_programs:training_plan_detail', training_plan_id=training_plan_id)
        return render(request, 'training_programs/create_training_plan_day.html',
                      {'form': form, 'training_plan': training_plan})
    else:
        form = ExerciseInPlanForm()
        form.fields['training_day'].queryset = training_day
    return render(request, 'training_programs/create_training_plan_day.html',
                  {'form': form, 'training_plan': training_plan})


@login_required
def training_plan_detail(request, training_plan_id):
    """
        Widok detali planu treningowego.
        Wyświetla szczegóły planu treningowego oraz dni treningowych przypisanych do tego planu.
        """
    training_plan = TrainingPlan.objects.get(pk=training_plan_id)
    training_days = training_plan.trainingday_set.all()

    context = {
        'training_plan': training_plan,
        'training_days': training_days,
    }

    return render(request, 'training_programs/training_plan_detail.html', context)


def display_exercises_view(request):
    """
        Widok wyświetlający listę ćwiczeń.
        """
    return render(request, 'training_programs/display_exercises.html', context={'exercises': Exercise.objects.all()})


@login_required
def view_training_plans(request):
    """
        Widok wyświetlający listę planów treningowych.
        """
    user = request.user
    if user.is_trainer:
        training_plans = TrainingPlan.objects.filter(trainer=user.id)
    else:
        training_plans = TrainingPlan.objects.filter(plan_owner_id=user.id)

    context = {'training_plans': training_plans}
    return render(request, 'training_programs/training_plan_list.html', context)


class AddExerciseFormView(FormView):
    """
        Widok formularza dodawania nowego ćwiczenia.
        """
    template_name = 'training_programs/create_exercise.html'
    form_class = AddExerciseForm
    success_url = '/exercises/'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)



class DisplayQuestionForPlan(ListView):
    """
       Widok wyświetlający listę pytań dotyczących planu treningowego.
       """
    model = TrainingPlanInfo
    template_name = 'training_programs/list_of_plan_questions.html'
    context_object_name = 'plan_question'


class QuestionForPlanDetailView(DetailView):
    """
        Widok detali pytania dotyczącego planu treningowego.
        """
    model = TrainingPlanInfo
    template_name = 'training_programs/plan_questions_detail.html'
    context_object_name = 'plan_question'


class ExerciseDetailView(DetailView):
    """
        Widok szczegółów ćwiczenia.
        Wyświetla szczegóły danego ćwiczenia.
        """
    model = Exercise
    template_name = 'training_programs/exercise_detail.html'
    context_object_name = 'exercise'


class PlanQuestionUpdateView(UpdateView):
    """
        Widok aktualizacji pytania dotyczącego planu treningowego.
        Umożliwia edycję istniejącego pytania dotyczącego planu treningowego.
        """
    model = TrainingPlanInfo
    template_name = "training_programs/edit_plan_question.html"
    fields = ['goals', 'time_of_one_training_in_minutes', 'amount_of_days', 'prefer_exercises']

    def get_success_url(self):
        return reverse_lazy('training_programs:plan_question_detail', kwargs={'pk': self.object.pk})


class PlanQuestionDeleteView(DeleteView):
    """
       Widok usuwania pytania dotyczącego planu treningowego.
       Umożliwia usunięcie istniejącego pytania dotyczącego planu treningowego.
       """
    model = TrainingPlanInfo
    template_name = "training_programs/delete_plan_question.html"
    success_url = reverse_lazy('training_programs:plan_request')
    context_object_name = 'object'
