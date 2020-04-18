from django.urls import path, include
from . import views

# handler404 = views.handler404
app_name = 'workouts'

urlpatterns = [
    path('',views.CreatedWorkoutListView.as_view(), name='workout_list'),
    path('<int:pk>/',views.show_workout, name='show_workout'),
    path('create_workout/',views.WorkoutCreateView.as_view(),name='create_workout'),
    path('<int:pk>/edit/', views.CreatedWorkoutUpdateView.as_view(),name='edit_workout'),
    path('<int:pk>/remove/', views.CreatedWorkoutDeleteView.as_view(),name='remove_workout'),
    path('<int:pk>/block_form/',views.WorkoutBlockCreateView.as_view(),name='create_block'),
    path('block/<int:pk>/edit/', views.WorkoutBlockUpdateView.as_view(),name='edit_block'),
    path('block/<int:pk>/remove/', views.WorkoutBlockDeleteView.as_view(),name='remove_block'),
    path('exercise_form/',views.WorkoutExerciseCreateView.as_view(),name='create_exercise'),
    path('exercise/<int:pk>/edit/', views.WorkoutExerciseUpdateView.as_view(),name='edit_exercise'),
    path('exercise/<int:pk>/remove/', views.WorkoutExerciseDeleteView.as_view(),name='remove_exercise'),
    # path('form_test/',views.create_workout, name='test_workout_form'),
]
