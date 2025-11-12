
from django.contrib.auth import views as auth_views
from .views import login_redirect  # importe sua função (ajuste o caminho conforme seu projeto)
from django.urls import path

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('redirect/', login_redirect, name='login_redirect'),

]
