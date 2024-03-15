from django.urls import path, include

from training_programs.views import create_training_plan_info, create_training_plan_day, display_exercises_view, \
    create_training_plan, view_training_plans, training_plan_detail, AddExerciseFormView, DisplayQuestionForPlan, \
    QuestionForPlanDetailView, ExerciseDetailView, PlanQuestionUpdateView, PlanQuestionDeleteView

app_name = 'training_programs'

urlpatterns = [
    path('ask-for-plan/', create_training_plan_info, name='plan_request'),
    path('create_training_plan/', create_training_plan, name='create_training_plan'),
    path('create-plan_day/<int:training_plan_id>', create_training_plan_day, name='add_exercise_to_plan'),
    path('view_training_plans/', view_training_plans, name='view_training_plans'),
    path('plan-details/<int:training_plan_id>', training_plan_detail, name='training_plan_detail'),
    path('exercises/', display_exercises_view, name='display_exercises'),
    path('add-exercise/', AddExerciseFormView.as_view(), name='add_exercise'),
    path('plan-questions/', DisplayQuestionForPlan.as_view(), name='plan_question'),
    path('plan-questions/<int:pk>', QuestionForPlanDetailView.as_view(), name='plan_question_detail'),
    path('exercise-detail/<int:pk>', ExerciseDetailView.as_view(), name='exercise_detail'),
    path('edit-plan-questions/<int:pk>', PlanQuestionUpdateView.as_view(), name='edit_plan_question'),
    path('delete-plan-questions/<int:pk>', PlanQuestionDeleteView.as_view(), name='delete_plan_question'),
]
