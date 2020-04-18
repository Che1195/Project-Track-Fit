from django.urls import path, include
from . import views

app_name = 'clientmanager'

urlpatterns = [
    path('', views.ClientListView.as_view(), name='client_list'),
    path('create_client/', views.ClientCreateView.as_view(), name='create_client'),
    path('<int:pk>/client_details/', views.show_client, name='client_details'),
    path('<int:pk>/edit/', views.ClientUpdateView.as_view(),name='edit_client'),
    path('<int:pk>/remove/', views.ClientDeleteView.as_view(),name='remove_client'),
    path('logged_workouts/', views.show_logged_workout_list, name='loggedworkout_list'),
    path('create_loggedworkout/', views.LoggedWorkoutCreateView.as_view(), name='create_loggedworkout'),
    path('logged_workout/<int:pk>/edit/', views.LoggedWorkoutUpdateView.as_view(),name='edit_loggedworkout'),
    path('logged_workout/<int:pk>/remove/', views.LoggedWorkoutDeleteView.as_view(),name='remove_loggedworkout'),
]
