from django import forms
from django.shortcuts import redirect

from .models import TrainingPlanInfo, ExerciseInPlan, TrainingPlan, TrainingDay, Exercise

INPUT_CLASSES = 'form-control'


class TrainingPlanInfoForm(forms.ModelForm):
    class Meta:
        model = TrainingPlanInfo
        fields = ['goals', 'time_of_one_training_in_minutes', 'amount_of_days', 'prefer_exercises']
        widgets = {'goals': forms.SelectMultiple(attrs={
            'class': INPUT_CLASSES,
        }),
            'time_of_one_training_in_minutes': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'amount_of_days': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'prefer_exercises': forms.SelectMultiple(attrs={
                'class': INPUT_CLASSES,
            }),
        }

        def post(self, request):
            if TrainingPlanInfo.objects.filter(user=request.user):
                return redirect('accounts:main')
            else:
                super().__init__(self)

class ExerciseInPlanForm(forms.ModelForm):
    class Meta:
        model = ExerciseInPlan
        fields = ['exercise', 'reps_amount', 'sets_amount', 'pause', 'tempo', 'training_day']


class TrainingPlanForm(forms.ModelForm):
    class Meta:
        model = TrainingPlan
        fields = '__all__'
        exclude = ('trainer',)
        widgets = {

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'amount_of_days': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'plan_owner': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'trainer': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
        }


class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
        widgets = {

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'types': forms.Select(),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'link_to_youtube': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }
