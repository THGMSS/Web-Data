from django.contrib import admin
from django.urls import path, include
from accounts.views import CustomLoginView
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    path('', lambda request: redirect('login')),
    path('accounts/', include('accounts.urls')),
    path('home/', include('home.urls')),
]
