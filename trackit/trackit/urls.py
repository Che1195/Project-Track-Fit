"""trackit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from exercise_database import views as exercise_database_views
from workouts import views as workout_views
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('test/',views.TestPage.as_view(),name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
    path('exercises/', exercise_database_views.ExerciseListView.as_view(), name='exercise_list'),
    path('admin/', admin.site.urls),
    path('exercise_database/', include('exercise_database.urls')),
    path('workouts/', include('workouts.urls')),
    path('clientmanager/',include('clientmanager.urls')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    # allows us to connect everything that django has under the hood for authorization
    path('acocunts/',include('django.contrib.auth.urls')),
]
