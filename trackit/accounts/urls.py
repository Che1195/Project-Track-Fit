from django.urls import path
# django has pre-built login and log out views that we can use
# we rename it so that it does not get mixed up with the views that we create
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('signup/',
         views.SignUp.as_view(),
         name='sign_up'),
    # path('create_client/',
    #      views.ClientCreateView.as_view(),
    #      name='create_client'),
    # path('client_list/',
    #      views.ClientListView.as_view(),
    #      name='client_list'),
]
