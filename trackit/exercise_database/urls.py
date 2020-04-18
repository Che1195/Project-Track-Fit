from django.urls import path, include
from . import views

app_name = 'exercise_database'

urlpatterns = [
    path('',views.ExerciseCreateView.as_view(),name='exercise_create'),
    path('exercise_list/', views.ExerciseListView.as_view(), name='exercise_list'),
    path('create/', views.ExerciseCreateView.as_view(), name='create'),
    path('details/<int:pk>/',views.ExerciseDetailView.as_view(), name='details'),
]
